amount_paid = 2000.0*40.0
purchase_commission = .03*amount_paid
sell_price = 2000.0*42.75
sell_commission = .03 * sell_price
total = sell_price - sell_commission - purchase_commission - amount_paid
print("The profit is: ", format(total,'.2f'))
