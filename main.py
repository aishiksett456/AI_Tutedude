import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package.billing import apply_tax

print("Discounted price: ",disc.apply_discount(1000,10))
print("Price after flat discount: ",disc.flat_discount(725))
print("Sum of prices: ",calculate_total([100,200,300]))
amount=int(input("Enter the amount: "))
print("Amount after Tax:",apply_tax(amount))