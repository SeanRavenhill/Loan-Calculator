import math


def exit_program(input):
    if input.lower() == "done" or input.lower() == "exit":
        print("\nProgram shutting down.\n")
        exit()
    else:
        pass


def monthly_payments():
    while True:
        print("\nEnter the loan principal:")
        loan = input()
        exit_program(loan)
        try:
            loan = int(loan)
            break
        except ValueError:
            print("\nInput Error. Please Try again.")

    while True:
        print("\nEnter the monthly payment:")
        payment = input()
        exit_program(payment)
        try:
            payment = int(payment)
            break
        except ValueError:
            print("\nInput Error. Please Try again.")

    while True:
        print("\nEnter the loan interest:")
        interest = input()
        exit_program(interest)
        if interest == 0:
            print("\nSorry calculator does not work with 0% interest loands.")
            monthly_payments()
        else:
            try:
                interest = int(interest)
                break
            except ValueError:
                print("\nInput Error. Please Try again.")

    rate = interest / (12 * 100)
    months = math.ceil(math.log((payment / (payment - rate * loan)), 1 + rate))
    y = math.floor(months / 12)
    m = months % 12

    if y >= 2 and m >= 2:
        print(f"\nIt will take {y} years and {m} months to repay this loan!")
    elif y == 1 and m >= 2:
        print(f"\nIt will take {y} year and {m} months to repay this loan!")
    elif y >= 2 and m == 1:
        print(f"\nIt will take {y} years and {m} month to repay this loan!")
    elif y == 0 and m >= 2:
        print(f"\nIt will take {m} months to repay this loan!")
    elif y == 0 and m == 1:
        print(f"\nIt will take {m} month to repay this loan!")
    elif y >= 2 and m == 0:
        print(f"\nIt will take {y} years to repay this loan!")
    elif y == 1 and m == 0:
        print(f"\nIt will take {y} year to repay this loan!")

    # if months == 1:
    # print(f"\nIt will take {months} month to repay the loan\n")
    # else:
    # print(f"\nIt will take {months} months to repay the loan\n")


def annuity():
    print("\nEnter the loan principal:")
    a = input()
    exit_program(a)


def principal():
    print("\nEnter the loan principal:")
    p = input()
    exit_program(p)


print("\nWhat do you want to calculate?")
print('\n- type "n" for number of monthly payments,')
print('- type "a" for annuity monthly payment amount,')
print('- type "p" for loan principal:')

while True:
    calc = input().lower()
    exit_program(calc)
    if calc == "n" or calc == "a" or calc == "p":
        break
    else:
        print("\nInput Error. Please Try again.")
        print('\n- type "n" for number of monthly payments,')
        print('- type "a" for annuity monthly payment amount,')
        print('- type "p" for loan principal:')

if calc == "n":
    monthly_payments()
elif calc == "a":
    annuity()
elif calc == "p":
    principal()
else:
    print("\nProgram Error. Shutting down.\n")


'''
    while True:
        n = input()
        exit_program(n)
        try:
            m = int(m)
            months = math.ceil(principal / m)
            break
        except ValueError:
            print("Input Error. Please Try again.\n")
    if months == 1:
        print(f"\nIt will take {months} month to repay the loan\n")
    else:
        print(f"\nIt will take {months} months to repay the loan\n")


while True:
    principal = input()
    exit_program(principal)
    try:
        principal = int(principal)
        break
    except ValueError:
        print("Input Error. Please Try again.\n")

while True:
    calc = input()
    exit_program(calc)
    if calc == "m" or calc == "p":
        break
    else:
        print("Input Error. Please Try again.")
        print('- type "m" - for number of monthly payments,')
        print('- type "p" - for the monthly payment:\n')

if calc == "m":
    print("Enter the monthly payment:")
    while True:
        m = input()
        exit_program(m)
        try:
            m = int(m)
            months = math.ceil(principal / m)
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
        exit_program(p)
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
'''
