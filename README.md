### RAG-Based-PDF_AI_Assistant
A context aware Retrieval-Augmented Generation (RAG) application allows users to ask questions about the PDF documents of a particular organisation and recieve factual answers related to the particular PDF. This project extracts text from pdf in form of chunks convert them into vector embeddings and stores them in local vector database, retrieves the most relevant vector w.r.t the query and uses as a context for the query. Google gemini is used to generate respose for the query strictly based on the retrieved context.

### Key Features

* Extracts text from PDF documents using pypdf.

* Splits large documents into small text chunks(nearly 400 words).

* Generates semantic embeddings with Google Gemini Embeddings API,thus generating a vector for each word.

* Stores embeddings persistently in ChromaDB.

* Performs similarity search to retrieve relevant document sections.

* Uses Gemini 2.5 Flash to answer questions grounded only in retrieved context.

* Provides a simple web interface built with Streamlit.

### Tech Stack

Frontend : Streamlit

AI & Embeddings : Google Gemini API

Vector Database : ChromaDB

PDF Processing : pypdf


### Project Structure

pdf-ai-assistant/

├── requirements.txt

├── day4_engine.py # PDF text extraction and chunking

├── day5_database.py # Embedding generation and storage

├── rag_core.py # Retrieval and answer generation

├── app.py # Streamlit web application

└── my_database/ # Persistent ChromaDB storage

### How It Works

1. Upload or place a PDF document in the project directory.

2. Extract and chunk the document text.

3. Generate embeddings for each chunk and store them in ChromaDB.

4. Convert user questions into embeddings.

5. Retrieve the most relevant chunks using vector similarity search.

6. Send the retrieved context to Gemini to generate a grounded answer.

### Use Cases

* Research paper question answering
  
* Document search and summarization
  
* Technical manual assistance
  
* Knowledge base creation
  
* Academic study support
