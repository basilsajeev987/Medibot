:::writing{variant="document" id="61482"}
# MediBot

## 🏥 AI-Powered Medical Chatbot using RAG

MediBot is an intelligent medical chatbot built using Retrieval-Augmented Generation (RAG), LangChain, Pinecone, Hugging Face Embeddings, and Mistral AI. The application enables users to ask medical questions in natural language and receive context-aware responses based on information retrieved from a medical knowledge base.

Instead of relying solely on a Large Language Model, MediBot retrieves relevant medical information from indexed documents stored in a Pinecone vector database, helping provide more accurate and grounded responses.

---

## 🚀 Features

- AI-powered medical question answering
- Retrieval-Augmented Generation (RAG)
- Semantic search using vector embeddings
- Pinecone Vector Database integration
- Mistral AI for response generation
- Medical document knowledge retrieval
- Context-aware responses
- Fast and scalable document search
- Interactive web-based chat interface
- Support for PDF-based medical knowledge bases

---

## 🏗️ Architecture

1. Medical documents are processed and converted into vector embeddings.
2. Embeddings are stored in Pinecone Vector Database.
3. Users submit questions through the web interface.
4. Relevant document chunks are retrieved from Pinecone.
5. Retrieved context is combined with the user query.
6. Mistral AI generates a contextual response.
7. The answer is returned to the user through the chatbot interface.

---

## 🛠️ Technology Stack

### Backend
- Python
- Flask
- LangChain

### AI & Machine Learning
- Mistral AI
- Hugging Face Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database
- Pinecone

### Frontend
- HTML
- CSS
- JavaScript
- Jinja2 Templates

### RAG Components
- Document Chunking
- Embedding Generation
- Semantic Search
- Context Retrieval
- Response Generation

---

## 📂 Project Structure

```text
MediBot/
│
├── app.py
├── requirements.txt
├── .env
│
├── src/
│   ├── helper.py
│   ├── prompt.py
│
├── templates/
│   └── chat.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── data/
├── research/
│
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/MediBot.git
cd MediBot
```

### Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
PINECONE_API_KEY=your_pinecone_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

---

## 🚀 Run the Application

```bash
python app.py
```

The application will be available at:

```text
http://localhost:8080
```

---

## 💬 Sample Queries

- What are the symptoms of diabetes?
- What causes hypertension?
- How is asthma treated?
- What are the complications of high blood pressure?
- Explain the stages of chronic kidney disease.
- What are the symptoms of pneumonia?

---

## 🔒 Disclaimer

MediBot is intended for educational, informational, and research purposes only.

The information provided by the chatbot should not be considered professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals regarding medical conditions or treatment decisions.

---

## 📈 Future Enhancements

- User authentication
- Chat history storage
- Multi-document support
- Source citations for responses
- Voice interaction
- Multi-language support
- Medical report analysis
- Cloud deployment
- Mobile application integration

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developed By

MediBot is developed using Flask, LangChain, Pinecone, Hugging Face Embeddings, and Mistral AI to provide intelligent medical document question answering through Retrieval-Augmented Generation (RAG).
:::
