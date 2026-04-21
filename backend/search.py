from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search_company(company: str):
   query = f"{company} company overview what does {company} do"

    response = client.search(query=query, max_results=5)

    results = response.get("results", [])

    if not results:
        return None

    # Prefer Wikipedia or Britannica if available
    for result in results:
        url = result["url"]
        if "britannica" in url:
            return url

    # fallback to first result
    return results[0]["url"]