import os
import chromadb
from google import genai

# Connect to resources
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))   #getting the connection with google studio
db_client = chromadb.PersistentClient(path="./my_database")  #getting the connection with my_database
collection = db_client.get_collection(name="pdf_collection") #getting access to 

def ask_pdf(user_question):
    # 1. Map the raw user query string into a mathematical vector mapping coordinate
    response = client.models.embed_content(model='gemini-embedding-2', contents=user_question) #it is a class
    query_vector = response.embeddings[0].values

    # 2. Search local database to isolate the top 2 closest matching text rows
    results = collection.query(query_embeddings=[query_vector], n_results=2)
    matched_paragraphs = results['documents'][0]
    context_text = "\n\n".join(matched_paragraphs)

    # 3. Formulate a highly restrictive prompt blueprint for the logic execution model
    final_prompt = f"""You are an absolute literal document assistant.
    Use ONLY the facts provided below to answer the question.
    If the answer is not explicitly written in the text context, say 'Fact unavailable.'
    Do not expand outside the text blocks and make sure the most important thing is that if question is from the documents asked 
    then please give a very long elloborated answer.

    Context from PDF:
    {context_text}

    Question: {user_question}
    Answer:"""

    # 4. Stream the strict instructions payload to the fast flash intelligence module
    ai_answer = client.models.generate_content(model='gemini-2.5-flash', contents=final_prompt)
    return ai_answer.text
