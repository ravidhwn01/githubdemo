import requests
from bs4 import BeautifulSoup


# Send an HTTP request to the URL of the webpage you want to access
url = "https://www.programiz.com/"
response = requests.get(url)

# Parse the HTML content of the page using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find the HTML elements that contain the data you want to extract
title = soup.find("title").text
paragraphs = soup.find_all("p")

# Print the extracted data
print("Title: " + title)
print("Paragraphs:")
for p in paragraphs:
    print(p.text)
