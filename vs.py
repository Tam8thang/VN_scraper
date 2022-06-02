from bs4 import BeautifulSoup as bs
import requests
import sys
import os

if len(sys.argv) != 2:
    sys.exit("enter the URL of a VNExpress' article")

try:
    with open("save_space.txt", "r") as save_space:
        space = save_space.read()

    URL = sys.argv[1]
    page = requests.get(URL)

    soup = bs(page.content, "lxml")

    date = soup.find("span", class_="date").text
    title = soup.find("h1", class_="title-detail").text
    desc =soup.find("p", class_="description").text
    parag = soup.find_all("p", class_="Normal")

    file_name = ""
    for i in range(len(title)):
        if title[i].isalnum() or title[i].isspace():
            file_name = file_name + title[i]

    file_path = space + file_name + ".txt"
    file = open(file_path, "w", encoding="utf-8")

    file.write(date + "\n\n")
    file.write(title + "\n\n")
    file.write(desc + "\n\n\n\n")
    for i in range(len(parag)):
        file.write(parag[i].text + "\n\n")
    file.write(URL)

    file.close()
    os.startfile(file_path)
except:
    print("The URL is invalid.")
