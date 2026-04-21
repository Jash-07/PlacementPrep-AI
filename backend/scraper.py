import requests
from bs4 import BeautifulSoup


def fetch_website_content(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        return None, response.status_code

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")
    text_data = [
        p.get_text().strip()
        for p in paragraphs
        if p.get_text().strip() != ""
    ]

    return text_data, 200