from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import system_prompt  # make sure system_prompt is defined
from langchain_mistralai import ChatMistralAI
import os
from langchain.chains import create_retrieval_chain
from langchain_huggingface import HuggingFaceEmbeddings

# -------------------- Flask setup --------------------
app = Flask(__name__)
load_dotenv()

# -------------------- API Keys --------------------
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY

# -------------------- Embeddings --------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-miniLM-L6-v2")
# -------------------- Pinecone Vector Store --------------------
index_name = "medical-bot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# -------------------- Mistral AI Chat Model --------------------
chat_model = ChatMistralAI(model="mistral-large-latest")  # use a supported model

# -------------------- Prompt Setup --------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# -------------------- RAG Chain --------------------
question_answer_chain = create_stuff_documents_chain(chat_model, prompt)
rag_chain = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=question_answer_chain
)
# -------------------- Flask Routes --------------------
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form.get("msg")
    if not msg:
        return "No input received", 400

    # Run RAG chain
    response = rag_chain.invoke({"input":msg})  # RetrievalQA uses `run` method
    print("Response:", response["answer"])
    return str(response)


# -------------------- Run Flask --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
