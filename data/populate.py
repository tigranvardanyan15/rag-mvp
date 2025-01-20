import requests
import json

from bs4 import BeautifulSoup

from app.db import db


PAGES_PATH = "data/pages.json"


if __name__ == "__main__":
    with open(PAGES_PATH, "r") as f:
        pages = json.load(f)

    for page in pages[:7]:
        response = requests.get(page["url"])

        soup = BeautifulSoup(response.content, "html.parser")
        raw_text = soup.get_text(separator="\n").strip()
        chunks = [line.strip() for line in raw_text.split("\n") if line.strip()]
        content = " ".join(chunks)

        success = db.add(id=page["name"], content=content, metadata=page)
        if not success:
            print(f"Error while inserting {page["name"]}")
