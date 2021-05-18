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
            loan = float(loan)
            break
        except ValueError:
            print("\nInput Error. Please Try again.")

    while True:
        print("\nEnter the monthly payment:")
        payment = input()
        exit_program(payment)
        try:
            payment = float(payment)
            break
        except ValueError:
            print("\nInput Error. Please Try again.")

    while True:
        print("\nEnter the loan interest:")
        interest = input()
        exit_program(interest)
        if float(interest) >= 12:
            print("\nInterest too high to be possible. Please try again.")
            monthly_payments()
        else:
            try:
                interest = float(interest)
                break
            except ValueError:
                print("\nInput Error. Please Try again.")

    if interest == 0:
        months = math.ceil(loan / payment)
        y = math.floor(months / 12)
        m = math.ceil(months % 12)
    else:
        rate = interest / (12 * 100)
        months = math.log((payment / (payment - rate * loan)), 1 + rate)
        y = math.floor(math.ceil(months / 12))
        m = math.ceil(months % 12)

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
