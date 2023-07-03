"""
This module provides the endpoints for the Wikipedia API, 
including a search endpoint and a wiki endpoint.
"""

from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki, wiki as wikilogic

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint that returns a message to indicate that the server is running.
    """

    return {"message": "Wikipedia API. Call /search or /wiki"}

@app.get("/search/{value}")
async def search(value: str):
    """
    Endpoint to search for a Wikipedia page using a given value.

    :param value: The value to search for.
    :return: The search result.
    """

    result = search_wiki(value)
    return {"result": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """
    Endpoint to retrieve a Wikipedia page using a given name.

    :param name: The name of the Wikipedia page to retrieve.
    :return: The retrieved Wikipedia page.
    """

    result = wikilogic(name)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
