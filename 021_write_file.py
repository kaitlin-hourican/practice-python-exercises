import requests
from bs4 import BeautifulSoup

def main():
    response = requests.get("https://www.nytimes.com/")
    content = response.text
    soup = BeautifulSoup(content, "html.parser")

    file_name = input("File name: ")

    with open(f"{file_name}.txt", "a") as file:
        file.write("NYT Article Tiles:\n")

        for title in soup.select("a.tpl-lbl div p"):
            file.write(f"  - {title.get_text(strip=True)}\n")


if __name__ == "__main__":
    main()