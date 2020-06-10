from products import Product

class Store:
    def __init__(self,name,products=[]):
        self.name = name
        self.products = []
    
    
    def display_products(self):
        for i in range(len(self.products)):
            print(f"{self.products[i].name}: ${self.products[i].price}")

    def add_product(self,new_product):
        self.products.append(new_product)
        return self    
    
    def sell_product(self,id):
        tempArr = []
        for i in self.products:
            if i == id:
                continue
            else:
                tempArr.append(i)
        self.products = tempArr    
    
    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)
       

    def set_clearance(self,category,percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)

               
 







    
    
    
    
    
    
        
        
        
        
        
            
    
        

        
        



     