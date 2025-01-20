from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.utils import filter_db_results
from app.settings import DEBUG
from app.db import db
from app.llm import llm_infer


app = FastAPI(
    debug=DEBUG,
)

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat")
async def chat_with_llm(request: Request, query: str = Form(...)):
    try:
        # Get results from vector database
        db_results = db.get(query)
        # Filter results which are fitting threashold
        context = filter_db_results(db_results)
        # Query llm
        result = llm_infer(query, context)

        response_text = result.get("answer", "No response text available")

        return templates.TemplateResponse(
            "index.html",
            {"request": request, "query": query, "response": response_text},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
