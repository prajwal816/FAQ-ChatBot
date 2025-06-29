## 🤖 Generative AI FAQ Chatbot

An AI-powered FAQ chatbot with a modern React frontend and FastAPI backend integrated with IBM Watsonx.ai for intelligent document-based question answering. Styled beautifully with Tailwind CSS and designed for real-time, responsive interactions.

---

### 🌟 Features

* 💬 **Conversational UI** - Modern WhatsApp-style chat interface
* 🤖 **IBM Watsonx.ai Integration** - Uses RAG to answer questions from your documents
* ⏳ **Real-time Feedback** - Typing indicators and loading states
* 📊 **Embeddings + Vector DB** - Built with `langchain`, `FAISS`, and `HuggingFace` models
* 🔧 **Customizable Knowledge Base** - Add your own `.txt`/`.md` FAQs
* 📊 **Auto-scroll + Timestamped Messages** - Smooth chat experience
* 🌐 **Responsive Design** - Works on all device sizes

---

### 🚀 Getting Started

#### 🚧 Backend Setup (FastAPI + LangChain + IBM Watsonx)

##### 1. Install dependencies

```bash
pip install -r requirements.txt
```

##### 2. Set environment variables (in `.env` file)

```env
IBM_API_KEY=your-api-key
IBM_PROJECT_ID=your-project-id
IBM_REGION=eu-de
IBM_MODEL_ID=google/flan-ul2
```

##### 3. Ingest the knowledge base

```bash
python ingest.py
```

##### 4. Run the backend

```bash
uvicorn main:app --reload --port 8000
```

Your backend is now live at: `http://localhost:8000`

#### Endpoint:

`POST /ask`

**Request:**

```json
{
  "query": "What is your return policy?"
}
```

**Response:**

```json
{
  "answer": "You can return products within 30 days of purchase."
}
```

#### Enable CORS in `main.py`

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### 🏠 Frontend Setup (React + TypeScript + Tailwind)

##### 1. Navigate to frontend directory

```bash
cd Frontend
```

##### 2. Install packages

```bash
npm install
```

##### 3. Start development server

```bash
npm run dev
```

Frontend will be served at: `http://localhost:8080`

---

### 🛏️ Project Structure

```
faq-chatbot/
├── Backend/
│   ├── main.py
│   ├── ingest.py
│   ├── chatbot.py
│   └── data/faqs/*.txt
├── Frontend/
│   ├── src/
│   │   ├── pages/Index.tsx
│   │   ├── main.tsx
│   │   └── lib/utils.ts
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
├── requirements.txt
└── README.md
```

---

### 🎨 Design Highlights

* Tailwind CSS powered components
* Lucide icons (`User`, `Bot`, `Send`, etc.)
* Smooth fade-in animations
* Typing dots animation when AI is thinking
* Blue-to-purple gradient header

---

### 🚨 Troubleshooting

**Error:** "Failed to get response from AI"

* Backend not running at `localhost:8000`
* Invalid IBM Watsonx credentials
* Missing vector store files (run `ingest.py` again)

**Frontend loads but no messages returned**

* Check backend logs for 500/400 errors
* Verify CORS is enabled

---

### 🦄 Future Additions

* 🌚 Dark mode toggle
* 🌍 Multi-language support
* 🔊 Voice input integration
* 📰 Chat history persistence
* 🔗 OAuth login

---

### 📚 License

MIT License. Feel free to fork and modify.

---

### 📤 Deploying

You can deploy the backend on **Render**, **Railway**, or **Heroku**.
Frontend can be deployed to **Vercel** or **Netlify**.

---

### 🔗 GitHub Repository

```bash
git init
git remote add origin https://github.com/your-username/FAQ-ChatBot.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

Made with ❤️ using React, FastAPI & IBM Watsonx.ai


### 📄 License

This project is open source and available under the **MIT License**.
