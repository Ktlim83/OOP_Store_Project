from store import Store
from products import Product



hat = Product("baseball_hat",10,"spring")
shirt = Product("t_shirt",20,"casual")
sock = Product("thermal_sock",5,"winter")
store = Store("Clothing Store")
store.add_product(hat).add_product(shirt).add_product(sock)

store.set_clearance("casual",10) 
store.display_products()

