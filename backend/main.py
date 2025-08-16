from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Allow CORS (optional, but useful if calling API from frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates setup
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize")
async def summarize(request: Request, meeting_text: str = Form(...)):
    # Temporary summarization logic (you can plug in AI model later)
    summary = "This is a placeholder summary of your meeting text."
    return templates.TemplateResponse(
        "index.html", {"request": request, "summary": summary, "meeting_text": meeting_text}
    )

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=10000, reload=True)
