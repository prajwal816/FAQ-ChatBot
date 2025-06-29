# Faq-chatbot

##Generative AI FAQ Chatbot – Full Stack (React + FastAPI)

A modern, responsive AI-powered FAQ chatbot with a sleek chat interface built in React + TypeScript and connected to a FastAPI backend using IBM Watsonx.ai. Features include real-time messaging, smooth animations, and seamless backend integration.

💡 Chatbot Preview
Imagine a WhatsApp-style chatbot UI that instantly replies using AI – all hosted locally!

✨ Features
💬 Modern Chat UI – Inspired by WhatsApp and Intercom

🤖 AI-Powered – Uses IBM Watsonx LLM via FastAPI backend

⏳ Loading States – Typing indicator + message delays

🌀 Smooth Animations – For real-time interaction feel

📱 Responsive – Works on desktop, tablet, and mobile

⏰ Timestamps – Shows when each message was sent

🚀 Auto-scroll – Scrolls to newest message on update

🎨 Beautiful UI – Gradient backgrounds, icons, and transitions

🚀 Getting Started
✅ Prerequisites
Node.js (v16 or higher)

Python 3.10+

pip (Python package manager)

uvicorn, fastapi, etc. (see requirements below)

🧠 Backend Setup (FastAPI + IBM Watsonx.ai)
Clone the project and navigate to the backend:

bash
Copy
Edit
cd faq-chatbot/Backend
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your IBM API environment variables (create a .env file):

ini
Copy
Edit
IBM_API_KEY=3nqGorN5PMhb9tOFO1ypA3a0-EllqF-AwJoLQbK3iCqM
IBM_PROJECT_ID=a4a4d653-ddc5-41b7-b06d-a43a66383b3a
IBM_REGION=eu-de
IBM_MODEL_ID=google/flan-ul2
Run the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload --port 8000
📍 Server runs at: http://localhost:8000

🌐 Frontend Setup (React + Vite)
Navigate to the frontend folder:

bash
Copy
Edit
cd ../Frontend
Install dependencies:

bash
Copy
Edit
npm install
Start the development server:

bash
Copy
Edit
npm run dev
Visit: http://localhost:8080

🏗️ Project Structure
bash
Copy
Edit
faq-chatbot/
├── Backend/              # FastAPI app with chatbot logic
│   ├── main.py
│   ├── chatbot.py
│   └── ...
├── Frontend/             # React + Vite frontend
│   ├── src/
│   │   ├── pages/
│   │   │   └── Index.tsx   # Main chat interface
│   │   ├── lib/
│   │   │   └── utils.ts
│   │   ├── index.css
│   │   └── main.tsx
│   └── ...
└── README.md
🎨 Design Highlights
📱 Responsive mobile-first layout

🎯 Tailwind CSS for styling

⌛ Bouncing dots typing animation

🌈 Gradient backgrounds & shadows

🔁 Real-time UX feel

🔧 Configuration
📡 Backend API
The React frontend connects to:

ts
Copy
Edit
const response = await fetch('http://localhost:8000/ask', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ query: inputText }),
});
🚨 Troubleshooting
🧩 Common Errors
"I'm having trouble connecting to my knowledge base"

✅ Fix:

Ensure uvicorn main:app is running

CORS is enabled in FastAPI:

python
Copy
Edit
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Frontend not loading
→ Make sure you're inside Frontend/ when running npm run dev.

🔮 Future Enhancements
🌙 Dark mode toggle

💾 Chat history persistence

🌍 Multi-language support

🔊 Voice input support

📄 Message export

📎 File uploads

❤️ Reactions on messages

📑 API Reference
POST /ask
Request:

json
Copy
Edit
{
  "query": "What are your delivery options?"
}
Response:

json
Copy
Edit
{
  "answer": "We offer standard and express delivery across India."
}
🤝 Contributing
Fork this repo

Create a new branch

Commit your features

Push and create a PR

📄 License
MIT License – use freely, contribute openly

### 📄 License

This project is open source and available under the **MIT License**.
