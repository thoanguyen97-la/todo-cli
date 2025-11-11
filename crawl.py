import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
with open ("data/quotes.txt","a",encoding="utf-8") as f:
    while True:
        response=requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes= soup.find_all("div",class_="quote")
        for q in quotes:
            quote=q.find("span",class_="text").get_text()
            author= q.find("small",class_="author").get_text()
            f.write(f"{author}: {quote}\n")
            f.write("-------------------------\n")
        next_button=soup.find("li",class_="next")
        if next_button:
            next_link= next_button.find("a").get("href")
            url= "https://quotes.toscrape.com"+ next_link
        else:
                break



