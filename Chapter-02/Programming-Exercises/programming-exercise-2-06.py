STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025
purchase_amount = float((input("Please enter the purchase amount: ")))
county_tax = float((COUNTY_SALES_TAX * purchase_amount))
state_tax = float((STATE_SALES_TAX * purchase_amount))
total = float((purchase_amount + county_tax + state_tax))
print("The total is: $"+format(total,'.2f'), "\n\tPurchase Amount = $"+format(purchase_amount,'.2f'), "\n\tState Tax = $"+format(state_tax,'.2f'), "\n\tCounty Tax = $"+format(county_tax,'.2f')) 
