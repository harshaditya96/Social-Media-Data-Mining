from bs4 import BeautifulSoup
#from urllib.request import urlopen
from urllib.request import urlopen

file = "cnn.csv"
f = open(file, "w")
Headers = "Headline,PublishDate,BodyContent\n"
f.write(Headers)

for page in range(1,7):
     url = "https://www.cnn.com/search/?q=donald+trump".format(page)
     html = urlopen(url)
     soup = BeautifulSoup(html,"html.parser")
     Title = soup.find_all("div", {"class":"cnn-search__result-contents"})
     for i in Title:
         try:
             headline = i.find("div", {"class":"cnn-search__result-headline"}).get_text()
             publishDate = i.find("div", {"class":"cnn-search__result-publish-date"}).get_text()
             bodyContent = i.find("div", {"class":"cnn-search__result-body"}).get_text()
             print(headline, publishDate, bodyContent)
             f.write("{}".format(headline).replace(",","|")+ ",{}".format(publishDate)+ ",{}".format(bodyContent).replace(",", " ")+ "\n")
         except: AttributeError
f.close()