from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from .models import Product
product_name = []
product_price = []
product_image = []
product_dict = {}

def crawler_code():
    my_url = "http://www.mega.pk/mobiles-apple/"
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    soup = BeautifulSoup(page_html, "html.parser")
    container = soup.findAll("body" > "div" > "ul" > "li" > "div" > "class" > "div", {"class": "wrapper1"})
    container2 = soup.findAll("body" > "div" > "ul" > "li" > "div", {"id": "lap_name_div"})
    container3 = soup.findAll("body" > "div" > "ul" > "li" > "div" > "div", {"class": "was"})
    for contname in container2:
        p_name = contname.h3.a
        name = p_name.text
        product_name.append(name)
    print(product_name)
    for contprice in container3:
        price = contprice.text
        product_price.append(price)
    print(product_price)
    for cont in container:
        # tag = cont.a
        # print(tag)
        image = cont.a.img["data-original"]
        product_image.append(image)
        print(product_image)
        product_dict = {
            "name": product_name,
            "price": product_price,
            "image": product_image
        }
        for i in range(len(product_dict)):
            models.Product.objects.create(
                prod_name=product_dict['name'][i],
                prod_price=product_dict['price'][i],
                prod_image=product_dict['image'][i])
        print("datasaved")


crawler_code()



    # Getting all the stuff from database
    #query_results = models.Product.objects.all()

    # Returning the rendered html
    #return django.shortcuts.render(request, "home.html")







