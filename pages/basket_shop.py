class Basket_shop:
    
    products=[]

    def add_to_basket(self, id, quantity, pay_option):
        self.products.append((id, quantity, pay_option))
        

    def del_from_basket(self, id):
        products_= self.products
        self.products = [x for x in products_ if x[0] != id]

