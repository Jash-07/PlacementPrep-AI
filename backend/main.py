from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "PlacementPrep AI Backend is running"}


@app.get("/scrape")
def scrape_website(company: str):
    if not company:
        raise HTTPException(status_code=400, detail="Company name is required")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Company page not found")

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")
        text_data = [
            p.get_text().strip()
            for p in paragraphs
            if p.get_text().strip() != ""
        ]

        return {
            "company": company,
            "url": url,
            "content_preview": text_data[:5]
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))