import requests as req
from bs4 import BeautifulSoup as bs
# import bs4 as bs

data = req.get("https://en.wikipedia.org/wiki/Leet#:~:text=Leet%20(or%20%221337%22),via%20reflection%20or%20other%20resemblance.")

if (data.status_code == 200):
    soup = bs(data.content,"html5lib");
    content_tab = soup.find_all("p")
    for i in content_tab:
        val = i.text.strip() #remove space
        for char in val:
            if (char.isnumeric()):
                continue
            else:
                print(char,end="");

       


