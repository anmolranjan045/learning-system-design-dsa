from discount_service import DiscountService
from diwali import DiwaliDiscount
from holi import HoliDiscount

diwa = DiwaliDiscount()
hol = HoliDiscount()

ds = DiscountService(diwa)
ds.process()
ds.update(hol)
ds.process()