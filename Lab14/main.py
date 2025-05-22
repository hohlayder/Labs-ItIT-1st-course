from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import wikipedia
from typing import Union

# Устанавливаем язык Wikipedia по умолчанию
wikipedia.set_lang("en")

app = FastAPI()

# Модели Pydantic для валидации запросов и ответов
class PageSummary(BaseModel):
    title: str
    summary: str

class ErrorResponse(BaseModel):
    error: str
    options: list[str] = []

class SearchInput(BaseModel):
    query: str

class PageContent(BaseModel):
    title: str
    content: str

@app.get("/page/{page_title}", response_model=Union[PageSummary, ErrorResponse])
def get_page_summary(path: str):
    """Получить краткое описание страницы Wikipedia по её названию"""
    try:
        page = wikipedia.page(path, auto_suggest=False)
        return PageSummary(title=page.title, summary=page.summary)
    except wikipedia.exceptions.DisambiguationError as e:
        return ErrorResponse(error="Уточните запрос", options=e.options)

@app.get("/search/")
def search_pages(query: str, limit: int = 3):
    """Поиск страниц Wikipedia с возможностью указания количества результатов"""
    results = wikipedia.search(query, results=limit)
    return {"query": query, "results": results}

@app.post("/page/", response_model=PageContent)
def get_page_content(search_input: SearchInput):
    """Получить полное содержание страницы Wikipedia"""
    try:
        # Берем первую страницу из результатов поиска
        page_title = wikipedia.search(search_input.query, results=1)[0]
        page = wikipedia.page(page_title, auto_suggest=False)
        return PageContent(title=page.title, content=page.content)
    except wikipedia.exceptions.DisambiguationError as e:
        raise HTTPException(status_code=400, detail={
            "error": "Уточните запрос",
            "options": e.options
        })