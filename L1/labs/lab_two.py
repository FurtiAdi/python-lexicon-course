salary = 26700
bonus = 3000
tax_rate = 0.34

total_income = salary + bonus
taxes = total_income * tax_rate
net_income = total_income - taxes

print(f"Net income before raise: {net_income}")

salary = 30000 # new salary

#Recalculate
total_income = salary + bonus
taxes = total_income * tax_rate
net_income = total_income - taxes

print(f"Net income after raise: {net_income}")