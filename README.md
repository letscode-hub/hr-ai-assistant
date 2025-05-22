# 🤖 HR AI Assistant

A Gemini-powered FastAPI web app that automates two critical HR processes:

- 📄 **Resume Screening** — Match candidate resumes to job descriptions
- 💬 **Sentiment Analysis** — Analyze employee feedback to detect attrition risk

🚀 **Live Demo**: [https://hr-ai-assistant-50ij.onrender.com](https://hr-ai-assistant-50ij.onrender.com)


---

## 🧠 Features

- FastAPI backend with Gemini 2.0 Flash LLM
- PDF + text resume parsing
- Clean JSON output from LLM
- Pretty web UI with Bootstrap dark theme
- Jinja2-based template rendering
- ✅ MIT licensed and ready for extension

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/hr-ai-assistant.git
cd hr-ai-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup API Key

Create a `.env` file in the root:

```env
GEMINI_API_KEY=your-google-ai-studio-key-here
```

> You can get this key from https://ai.google.dev

### 4. Run the App

```bash
uvicorn app.main:app --reload
```

Then open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Project Structure

```
hr-ai-assistant/
├── app/
│   ├── main.py
│   ├── templates/
├── resume_screening/
├── sentiment_analysis/
├── utils/
├── .env.example
├── .render.yaml
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📤 Deployment (Render)

1. Push this repo to GitHub
2. Add your `GEMINI_API_KEY` in the Render dashboard as an environment variable
3. Use the `.render.yaml` config for automated deployment

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE)

---

## 🙌 Author

Nivedita Agarwal  
Feel free to fork, star, and use it for your own AI tools or HR experiments 🚀
