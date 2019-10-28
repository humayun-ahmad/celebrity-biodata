import requests
from bs4 import BeautifulSoup as bf

# link :
url = "https://www.imdb.com/search/name/?gender=male,female&ref_=nv_tp_cel"

i = 1
# cnt = 0

# start here to find each celebrity link:
while(i <= 2000):

	Response = requests.get(url)

	soup = bf(Response.text,'lxml')

	divs = soup.find_all('div', class_ = "lister-item-content")
	
	for div in divs:

	    a_tags = div.findChildren('a')


	    for a_tag in a_tags:
	        f = open("celebrity_Link.txt","a")
	        f.write("https://www.imdb.com" + a_tag['href'] + "\n")
	        # cnt = cnt + 1
	        # print (a_tag['href'])
	        break

	nextlink = soup.find('a', class_ = "lister-page-next next-page")
	url = "https://www.imdb.com" + nextlink['href']

	# print(url)
	# break
	i = i + 1


