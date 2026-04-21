from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "PlacementPrep AI Backend is running"}


@app.get("/scrape")
def scrape_website():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        # Check if request was successful
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch the webpage")

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract paragraph text
        paragraphs = soup.find_all("p")
        text_data = [
            p.get_text().strip()
            for p in paragraphs
            if p.get_text().strip() != ""
        ]

        return {
            "url": url,
            "total_paragraphs": len(text_data),
            "content_preview": text_data[:5]
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))