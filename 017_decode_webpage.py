import requests
from bs4 import BeautifulSoup

def main():
    print("NYT Article Tiles: ")
    response = requests.get("https://www.nytimes.com/")
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    for title in soup.select("a.tpl-lbl div p"):
        print("  -  ", title.get_text(strip=True))


if __name__ == "__main__":
    main()