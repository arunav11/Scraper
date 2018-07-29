from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url= 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
# opening the connection,grabbing the page
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()

# html_parsing
page_soup = soup(page_html, "html.parser")
filename="products.csv"
f=open(filename,"w")
headers="S.No.,Brand,Product_name,Shipping\n"
f.write(headers)
# grabs each product
containers = page_soup.find_all("div",{"class":"item-container"})
i=1
for container in containers:
    brand = container.div.div.a.img["title"]
    title_container = container.find_all("a",{"class": "item-title"})
    product_name = title_container[0].text
    shipping_container = container.find_all("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    print("Brand : "+ brand +" Product :"+ product_name+" Shipping :"+ shipping)
    f.write("%d , %s, %s , %s \n" %(i,brand,product_name.replace(",","|"),shipping))
    i=i+1
f.close()