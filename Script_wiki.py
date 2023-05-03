import os
import requests
from bs4 import BeautifulSoup
from time import sleep
# take the info form wiki
url = "https://en.wikipedia.org/wiki/List_of_animal_names"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
#selects all the rows in the table
table = soup.find("table", {"class": "wikitable sortable"})
rows = table.find_all("tr")[1:]
#Open desktop and create there file name "animal_names".
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
filename = os.path.join(desktop_path, "animal_names.txt")
#take all the input and put on the file "animal_names"
with open(filename, "w") as file:
    for row in rows:
        cols = row.find_all("td")
        animal = cols[0].text.strip()
        collective_nouns = cols[1].text.strip().split(", ")
        collateral_adjective = cols[2].text.strip()

        if collective_nouns == [""]:
            file.write(f"{animal} - {collateral_adjective}\n")
        else:
            for collective_noun in collective_nouns:
                file.write(f"{animal} - {collective_noun}\n")
