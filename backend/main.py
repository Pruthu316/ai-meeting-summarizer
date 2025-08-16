from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import resend
from groq import Groq

# init
app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
resend.api_key = os.getenv("RESEND_API_KEY")

# templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request, transcript: str = Form(...), prompt: str = Form(...)):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an AI meeting summarizer."},
            {"role": "user", "content": f"Transcript:\n{transcript}\n\nInstruction:\n{prompt}"}
        ],
    )
    summary = response.choices[0].message.content
    return templates.TemplateResponse("index.html", {"request": request, "summary": summary, "transcript": transcript})

@app.post("/share")
async def share(request: Request, recipients: str = Form(...), summary: str = Form(...)):
    resend.Emails.send({
        "from": os.getenv("FROM_EMAIL"),
        "to": recipients.split(","),
        "subject": "Meeting Summary",
        "html": f"<pre>{summary}</pre>",
    })
    return templates.TemplateResponse("index.html", {"request": request, "summary": summary, "message": "✅ Email sent!"})
                      
