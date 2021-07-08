TIP = 0.18
TAX = 0.07
total_amount = float(input("How much is the total: "))
tip = TIP * total_amount
tax = TAX * total_amount
print("GRAND TOTAL = $" + format(total_amount+tip+tax,'.2f'), "\n\tPURCHASE = $" + format(total_amount, '.2f'), "\n\tTIP = $" + format(tip,'.2f'), "\n\tTAX = $" + format(tax,'.2f'))
