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
