import math

print("Enter the loan principal:")

while True:
    principal = input()
    if principal.lower() == "done" or principal.lower() == "exit":
        exit()
    else:
        try:
            principal = int(principal)
            break
        except ValueError:
            print("Input Error. Please Try again.\n")


print("\nWhat do you want to calculate?")
print('- type "m" - for number of monthly payments,')
print('- type "p" - for the monthly payment:\n')

while True:
    calc = input()
    if calc.lower() == "done" or calc.lower() == "exit":
        exit()
    elif calc == "m" or calc == "p":
        break
    else:
        print("Input Error. Please Try again.")
        print('- type "m" - for number of monthly payments,')
        print('- type "p" - for the monthly payment:\n')

if calc == "m":
    print("Enter the monthly payment:")
    while True:
        m = input()
        if m.lower() == "done" or m.lower() == "exit":
            exit()
        else:
            try:
                m = int(m)
                months = int(round(principal / m, 0))
                break
            except ValueError:
                print("Input Error. Please Try again.\n")
    if months == 1:
        print(f"\nIt will take {months} month to repay the loan\n")
    else:
        print(f"\nIt will take {months} months to repay the loan\n")
else:
    print("Enter the number of months:")
    while True:
        p = input()
        if p.lower() == "done" or p.lower() == "exit":
            exit()
        else:
            try:
                p = int(p)
                pay = math.ceil(principal / p)
                uneven_div = principal % p
                last = principal - (pay * (p - 1))
                break
            except ValueError:
                print("Input Error. Please Try again.\n")
    if uneven_div:
        print(f"Your monthly payment = {pay} and the last payment = {last}.")
    else:
        print(f"Your monthly payment = {pay}")
