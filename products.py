class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        
    def update_price(self, percent_change, is_increased):
        percent_change = percent_change/100
        if is_increased == True:
            self.price = self.price + self.price*percent_change
        elif is_increased == False:
            self.price = self.price - self.price*percent_change
            
    def print_info(self):
        print(f"{self.name}:${self.price}") 
    
