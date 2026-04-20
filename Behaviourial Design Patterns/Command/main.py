from chef import Chef
from waiter import Waiter
from pizza_order import PizzaOrder
from cook_pasta import PastaOrder

chef = Chef()
piz_ord = PizzaOrder(chef)

wt = Waiter()
wt.take_order(piz_ord)