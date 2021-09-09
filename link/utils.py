import requests
from bs4 import BeautifulSoup
import lxml
#url="https://www.amazon.in/Airdopes-121v2-Bluetooth-Immersive-Assistant/dp/B08JQN8DGZ?ref_=Oct_DLandingS_D_7a07edf6_60&smid=A14CZOWI0VEHLG"

#headers={
	
	#"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
	#"Accept-Language":"en",
#}

#r=requests.get(url,headers=headers)

#soup=BeautifulSoup(r.text,"lxml")

#print(soup.prettify())

#price=soup.select_one(selector="#priceblock_dealprice").getText()
#name=soup.select_one(selector="#productTitle").getText()
#name=name.strip()
#price=price.strip()
#priceblock_dealprice
#productTitle
#print(name)
#print(price)


def get_link_data(url):

	headers={
		
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
		"Accept-Language":"en",
	}

	r=requests.get(url,headers=headers)

	soup2=BeautifulSoup(r.text,"lxml")

	#print(soup.prettify())

	price=soup2.select_one(selector="#priceblock_ourprice").getText()
	name=soup2.select_one(selector="#productTitle").getText()
	name=name.strip()
	price=price.strip()
	price=price.replace(",","")
	price=float(price[1:])
	return name,price
