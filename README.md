# Project 04: Web Scraper for Headlines & Quotes

## Project Overview
A Python-based web scraping application that extracts quotes, author names, and tags from a website using Requests and BeautifulSoup. It supports multiple-page scraping and saves the collected data into JSON and TXT files.

## Features
- Connects to websites using HTTP requests.
- Extracts webpage content using BeautifulSoup.
- Collects quotes and author names.
- Extracts tags associated with each quote.
- Supports multiple-page scraping.
- Saves extracted information into JSON format.
- Saves extracted information into readable TXT format.
- Handles HTTP request errors.

## Technologies Used
- Python 3.12
- Requests
- BeautifulSoup4
- JSON
- HTML

## Project Structure
```text
Project_04_Web_Scraper/
│
├── web_scraper.py
├── quotes.json
├── quotes.txt
└── README.md
```

## Installation

Install the required libraries:

```bash
python -m pip install requests beautifulsoup4
```

## How to Run

Run the following command:

```bash
python web_scraper.py
```

## Expected Output
- Extracts up to 100 quotes from multiple pages.
- Displays the number of pages scraped.
- Displays the total number of quotes extracted.
- Creates `quotes.json` and `quotes.txt` files.

## Learning Outcomes
- Understanding HTTP requests and responses.
- Learning HTML structure and tag inspection.
- Extracting website data using BeautifulSoup.
- Understanding pagination in web scraping.
- Working with JSON and TXT file handling.
- Learning practical Python data collection techniques.

## Author
Kishore

## Practice Website
https://quotes.toscrape.com/