base = int(input("Enter a number: "))
exponent = int(input("Enter again other number: "))
power=1

i=0
while i<exponent:
  power *= base 
  i+=1

print(f"{base} to the power of {exponent} is {power}")
