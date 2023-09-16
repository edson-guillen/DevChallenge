from twilio.rest import Client
from tokens import tokens

client = Client(tokens["account_sid"], tokens["auth_token"])

class Product:
    def __init__(self, product_name, price, time, quantity, link) -> None:
        self.product_name = product_name
        self.price = price
        self.time = time
        self.quantity = quantity
        self.link = link

class User:
    def __init__(self, phone, email) -> None:
        self.phone = phone
        self.email = email
        self.products = []
        
    def addProduct(self, product):
        self.products.append(product)
        
    def sendSMS(self):
        item_valor = {prod.product_name:prod.price for prod in self.products}
        str_produtos = ""
        for i,item in enumerate(item_valor):
            str_produtos += f"Produto: {item}" + f"Preço: {item_valor[item]}" + "\n"
        message = client.messages.create(
            from_='+15078733409',
            body=f"""Opa! Acho que você esqueceu o seu produto no carrinho! Aproveite agora para finalizar sua compra! Aqui estão os produtos deixados no carrinho:
            {str_produtos}

            """,
            to=self.phone
        )
        return message
    
    def sendWhatsappMessage(self):
        item_valor = {prod.product_name:prod.price for prod in self.products}
        str_produtos = ""
        for i,item in enumerate(item_valor):
            str_produtos += f"Produto: {item}" + f"Preço: {item_valor[item]}" + "\n"
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"""Opa! Acho que você esqueceu o seu produto no carrinho! Aproveite agora para finalizar sua compra! Aqui estão os produtos deixados no carrinho:
            {str_produtos}

            """,
            to=f'whatsapp:{self.phone}'
        )
        return message
    