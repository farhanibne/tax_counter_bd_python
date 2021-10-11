ammount = float(input("Enter Total Ammount Of Money IN Taka :  "))
tax = 0.0

if (ammount <= 300000):
    tax = 0
elif (ammount <= 400000):
    if (ammount < 300000):
        tax = 0
    elif(ammount <=400000):
        tax = (ammount - 300000)*5/100
elif (ammount <= 700000):
    if (ammount < 300000):
        tax = 0
    else:

        f_a = (ammount - 300000)
        s_a = (ammount - 400000)
        tax_1 = (100000 * 5/100)
        tax_2 = (s_a * 10/100)
        tax = (tax_1 + tax_2)
elif (ammount <= 1100000):
    if (ammount < 300000):
        tax = 0
    else:
       d_a = (ammount - 700000)
       tax_1 = (100000 * 5/100)
       tax_2 = (300000 * 10/100)
       tax_3 = (d_a * 15/100)
       tax = (tax_1 + tax_2 + tax_3)

elif (ammount < 1600000):
    if (ammount < 300000):
        tax = 0
    else:
       p_a = (ammount - 1100000)
       tax_1 = (100000 * 5/100)
       tax_2 = (300000 * 10/100)
       tax_3 = (400000 * 15/100)
       tax_4 = (p_a * 20/100)
       tax = (tax_1 + tax_2 + tax_3 + tax_4)

elif (ammount >= 1600000):
    if (ammount < 300000):
        tax = 0
    else:
       l_a = (ammount - 1600000)
       tax_1 = (100000 * 5/100)
       tax_2 = (300000 * 10/100)
       tax_3 = (400000 * 15/100)
       tax_4 = (700000 * 20/100)
       tax_5 = (l_a * 25/100)-40000
       tax = (tax_1 + tax_2 + tax_3 + tax_4 + tax_5)




print(f"Your Payable Tax Is :: {tax}")
