import tabula
import requests
from bs4 import BeautifulSoup

URL = "https://www.udesc.br/cct/restaurante/cardapio"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

link_ok = 0

while(link_ok == 0):
    for a_href in soup.find_all("a", href=True):
        link = a_href["href"]
        if link[:43] == "https://www.udesc.br/arquivos/cct/id_cpmenu":
            cardapio_link = a_href["href"]
            print(cardapio_link)
            link_ok = link_ok + 1

file_url = cardapio_link
  
r = requests.get(file_url, stream = True) 
  
with open("cardapio.pdf","wb") as pdf: 
    for chunk in r.iter_content(chunk_size=1024): 
 
         if chunk: 
             pdf.write(chunk) 

df = tabula.read_pdf('cardapio.pdf', pages = 'all')[0]

df.to_excel('cardapio.xlsx')