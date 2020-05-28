import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
product_name = []
product_price = []
product_image = []
class products:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def crawler_code(self):
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
            #tag = cont.a
            #print(tag)
            image = cont.a.img["data-original"]
            product_image.append(image)
        print(product_image)
        product_dict = {
            "name" : product_name,
            "price" : product_price,
            "image" : product_image
        }
        print(product_dict)
        dic_length = len(product_dict["name"])
        print(dic_length)
        self.store_db(product_dict)
    def create_connection(self):
        self.conn = sqlite3.connect("products.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""Drop table if exists products_tb""")
        self.curr.execute("""Create table products_tb(
                        name text,
                        price text,
                        image text
                        )""")



    def store_db(self,product_dict):
        for i in range(len(product_dict['price'])):
            self.curr.execute("""insert into products_tb values(?,?,?)""", (
                product_dict['name'][i],
                product_dict['price'][i],
                product_dict['image'][i]
            ))
        self.conn.commit()

def main():
    p = products()
    r1 = p.crawler_code()


if __name__ == "__main__":
    main()


