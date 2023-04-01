# a4.py
# Carrie Liu
# carrihl1@uci.edu
# 64814057

import requests
import json

API_ENDPOINT = "https://www.googleapis.com/books/v1/volumes"
MAX_RESULTS = 5

def search_books(query):
    params = {
        "q": query,
        "maxResults": MAX_RESULTS
    }
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()
    books = data.get("items", [])
    results = []
    for book in books:
        title = book.get("volumeInfo", {}).get("title", "Unknown Title")
        authors = book.get("volumeInfo", {}).get("authors", [])
        author = authors[0] if authors else "Unknown Author"
        results.append((title, author))
    return results

def main():
    query = input("Enter a search query: ")
    results = search_books(query)
    print("Search results:")
    for title, author in results:
        print("- {} by {}".format(title, author))

if __name__ == '__main__':
    main()
