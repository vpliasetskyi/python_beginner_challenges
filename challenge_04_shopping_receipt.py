item1_name = str(input("Enter item 1 name: "))
item1_price = float(input("Enter item 1 price: "))
item2_name = str(input("Enter item 2 name: "))
item2_price = float(input("Enter item 2 price: "))
item3_name = str(input("Enter item 3 name: "))
item3_price = float(input("Enter item 3 price: "))

total_price = item1_price + item2_price + item3_price
print(
"-----------------------\n"    
f"{item1_name:<10}:${item1_price:>6.2f}\n"
f"{item2_name:<10}:${item2_price:>6.2f}\n"
f"{item3_name:<10}:${item3_price:>6.2f}\n"
"-----------------------\n"
f"{'Total':<10}:${total_price:>6.2f}"
)