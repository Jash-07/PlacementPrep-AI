from fastapi import FastAPI, HTTPException
from scraper import fetch_website_content

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "PlacementPrep AI Backend is running"}


@app.get("/scrape")
def scrape_website(company: str):

    if not company:
        raise HTTPException(status_code=400, detail="Company name is required")

    url = f"https://en.wikipedia.org/wiki/{company}"

    content, status = fetch_website_content(url)

    if status != 200:
        raise HTTPException(status_code=status, detail="Failed to fetch webpage")

    return {
        "company": company,
        "url": url,
        "content_preview": content[:5]
    }