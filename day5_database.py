import os
import chromadb
from google import genai
from day4_engine import chunks  # Pulls the active chunk blocks directly from Day 4 script

# 1. Connect to Google's backend infrastructure client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Instantiate a permanent local disk database folder instance on your machine
db_client = chromadb.PersistentClient(path="./my_database")
collection = db_client.get_or_create_collection(name="pdf_collection")

print("Connecting to Gemini API to translate text blocks into math coordinates...")

# 3. Step through every isolated sentence block systematically
for index, text_block in enumerate(chunks):
    # Request an embedding calculation response matrix
    response = client.models.embed_content(
        model='gemini-embedding-2',
        contents=text_block
    )
    vector_numbers = response.embeddings[0].values

    # Write text block and mathematical coordinate array together to the database disk
    collection.add(
        ids=[f"id_{index}"],
        embeddings=[vector_numbers],
        documents=[text_block]
    )

print("System Success: All text arrays are permanently indexed to your hard drive folder!")
