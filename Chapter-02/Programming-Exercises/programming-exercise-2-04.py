SALES_TAX = .07
price_i1 = float(input("What is the price of item 1?\n"))
price_i2 = float(input("What is the price of item 2?\n"))
price_i3 = float(input("What is the price of item 3?\n"))
price_i4 = float(input("What is the price of item 4?\n"))
price_i5 = float(input("What is the price of item 5?\n"))
price_total = price_i1 + price_i2 + price_i3 + price_i4 + price_i5
tax_total = float(format(SALES_TAX * price_total, '.2f'))
total = price_total + tax_total
print("The total price comes to:", total, "\n Subtotal:", price_total, "\n Tax:", tax_total)
