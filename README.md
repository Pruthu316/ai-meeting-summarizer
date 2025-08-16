# AI Meeting Notes Summarizer & Sharer

This project is an **AI-powered meeting notes summarizer** where you can:
- Upload transcripts (meeting notes, call transcripts, etc.)
- Enter a custom instruction/prompt (e.g., "Summarize in bullet points")
- Generate editable summaries
- Share them via email

---

## 🚀 Deploy to Render

Click the button below to deploy your own instance:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

---

## 🔑 Environment Variables

Before running locally or on Render, set these:

| Variable       | Description                            |
|----------------|----------------------------------------|
| `GROQ_API_KEY` | Your Groq API key (starts with `gsk_`) |
| `RESEND_API_KEY` | Your Resend API key (starts with `re_`) |
| `FROM_EMAIL`   | Verified sender email for Resend       |

---

## 🖥 Local Development

1. Clone the repo  
   ```bash
   git clone https://github.com/Pruthu316/ai-meeting-summarizer.git
   cd ai-meeting-summarizer
