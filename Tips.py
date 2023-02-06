print ("How many pennies: ", end='')
pennies = input()

print ("How many nickels: ", end='')
nickels = input()

print ("How many dimes: ", end='')
dimes = input()

print ("How many quarters: ", end='')
quarters = input()

print ("How many dollars: ", end='')
dollars = input()

Tips = (float(pennies)*0.01) + (float(nickels)*0.05) + (float(dimes)*0.10) + (float(quarters)*.25) + (float(dollars)*1.00)

print ("Total: "+str('%.2f' % Tips))