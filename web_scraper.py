
import requests
import json
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://quotes.toscrape.com/"
all_quotes = []

page_number = 1
max_pages = 10

try:
    while url and page_number <= max_pages:

        print(f"Scraping page {page_number}...")

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text

            tags = quote.find_all("a", class_="tag")
            tag_names = [tag.text for tag in tags]

            all_quotes.append({
                "quote": text,
                "author": author,
                "tags": tag_names
            })

        next_link = soup.find("li", class_="next")

        if next_link:
            next_url = next_link.find("a")["href"]
            url = urljoin(url, next_url)
            page_number += 1
            time.sleep(1)
        else:
            url = None

    # Save JSON file
    with open("quotes.json", "w", encoding="utf-8") as file:
        json.dump(all_quotes, file, indent=4, ensure_ascii=False)

    # Save TXT file
    with open("quotes.txt", "w", encoding="utf-8") as file:
        for item in all_quotes:
            file.write("Quote: " + item["quote"] + "\n")
            file.write("Author: " + item["author"] + "\n")
            file.write("Tags: " + ", ".join(item["tags"]) + "\n")
            file.write("-" * 50 + "\n")

    print("\nScraping completed!")
    print("Total pages:", page_number)
    print("Total quotes extracted:", len(all_quotes))
    print("JSON file saved successfully!")
    print("TXT file saved successfully!")

except requests.exceptions.RequestException as error:
    print("Website connection error:", error)
