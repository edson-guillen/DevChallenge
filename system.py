import requests
import user_product
from datetime import datetime

carts = list()
with open("carts.txt", "r") as arq:
    for i, line in enumerate(arq):
        carts.append(line.replace("\n", ""))

users = list()
for i,item in enumerate(carts):
    response = requests.get(item).json()    
    user_atual = user_product.User(response[0]["Cart"]["phone"],response[0]["Cart"]["email"])
    users.append(user_atual)
    for prod in response:
        time = prod["Cart"]["date"] + " " + prod["Cart"]["hour"]
        date_time = datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
        user_atual.addProduct(user_product.Product(prod["Cart"]["product_name"],
                                            prod["Cart"]["price"],            
                                            date_time,
                                            prod["Cart"]["quantity"],
                                            prod["Cart"]["product_url"]["https"]))

for user_product in users:
    user_product.sendSMS()
    user_product.sendWhatsappMessage()
