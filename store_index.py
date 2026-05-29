from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_hugging_face_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

# -------------------- Load environment variables --------------------
load_dotenv()
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY

# -------------------- Load & process PDFs --------------------
extracted_data = load_pdf_file(data="data/")
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(filter_data)

# -------------------- Generate embeddings --------------------
embeddings = download_hugging_face_embeddings()

# -------------------- Initialize Pinecone --------------------
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-bot"

# Create index if it doesn't exist
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,            # embedding dimension
        metric="cosine",          # corrected parameter
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

index = pc.Index(index_name)

# -------------------- Store embeddings in Pinecone --------------------
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)

print(f"✅ Indexed {len(text_chunks)} document chunks into Pinecone '{index_name}'")
