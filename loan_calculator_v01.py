import math


def main():
    print("What do you want to calculate?")
    print('\n- type "a" for annuity monthly payment amount.')
    print('- type "n" for number of monthly payments.')
    print('- type "p" for loan principal.')
    print('- type "d" for differentiated payments.')

    while True:
        calc = input().lower()
        exit_program(calc)
        if calc == "n" or calc == "d" or calc == "a" or calc == "p":
            break
        else:
            print("\nInput Error. Please Try again.")
            print('\n- type "a" for annuity monthly payment amount.')
            print('- type "n" for number of monthly payments.')
            print('- type "p" for loan principal.')
            print('- type "d" for differentiated payments.')

    if calc == "n":
        monthly_payments()
    elif calc == "d":
        differentiated()
    elif calc == "a":
        annuity()
    elif calc == "p":
        principal()
    else:
        print("\nProgram Error. Shutting down.\n")


def exit_program(input):
    if input.lower() == "done" or input.lower() == "exit":
        print("\nProgram shutting down.\n")
        exit()
    else:
        pass


def loan_principal():
    while True:
        print("\nEnter the loan principal:")
        loan = input()
        exit_program(loan)
        try:
            loan = float(loan)
            break
        except ValueError:
            print("\nInput Error. Please Try again.")

    return loan


def monthly_payment():
    while True:
        print("\nEnter the monthly payment:")
        payment = input()
        exit_program(payment)
        try:
            payment = float(payment)
            break
        except ValueError:
            print("\nInput Error. Please Try again.")

    return payment


def loan_interest():
    while True:
        print("\nEnter the loan interest:")
        interest = input()
        exit_program(interest)
        try:
            interest = float(interest)
            break
        except ValueError:
            print("\nInput Error. Please Try again.")

    return interest


def payment_period():
    while True:
        print("\nEnter the number of periods:")
        periods = input()
        exit_program(periods)
        try:
            periods = float(periods)
            break
        except ValueError:
            print("\nInput Error. Please Try again.")

    return periods


def annuity_payment():
    while True:
        print("\nEnter the annuity payment:")
        annuity_payment = input()
        exit_program(annuity_payment)
        try:
            annuity_payment = float(annuity_payment)
            break
        except ValueError:
            print("\nInput Error. Please Try again.")

    return annuity_payment


def monthly_payments():
    loan = loan_principal()
    payment = monthly_payment()
    interest = loan_interest()
    y = 0
    m = 0

    if interest == 0:
        months = math.ceil(loan / payment)
        y = math.floor(months / 12)
        m = math.ceil(months % 12)
        if m == 12:
            y += 1
            m = 0
    else:
        rate = interest / (12 * 100)
        log_check = payment - (rate * loan)
        if log_check <= 0:
            print("\nLoan at interest rate not possible. Please try again.")
            monthly_payments()
        else:
            base = payment / (payment - rate * loan)
            months = math.log(base, 1 + rate)
            y = math.floor(months / 12)
            m = math.ceil(months % 12)
            if m == 12:
                y += 1
                m = 0

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

    total_payments = int(payment * ((y * 12) + m))
    overpayment = int(total_payments - loan)

    if overpayment > 0:
        print(f"\nOverpayment = {overpayment}")


def annuity():
    loan = loan_principal()
    n = payment_period()
    i = loan_interest()

    total_payments = 0

    if i == 0:
        annuity = math.ceil(loan / n)
        last = int(round((loan % annuity), 0))
        total_payments += ((annuity * n) - annuity) + last
        if last:
            print(f"\nYour monthly payment = {annuity} and the last payment"
                  f" = {last}!")
        else:
            print(f"\nYour monthly payment = {annuity}!")
    else:
        r = i / (12 * 100)
        annuity = loan * ((r * ((1 + r) ** n)) / (((1 + r) ** n) - 1))
        annuity = math.ceil(annuity)
        last = int(round((loan % annuity), 0))
        total_payments += ((annuity * n) - annuity) + last
        if last:
            print(f"\nYour monthly payment = {annuity} and the last payment"
                  f" = {last}!")
        else:
            print(f"\nYour monthly payment = {annuity}!")

    overpayment = int(total_payments - loan)

    if overpayment > 0:
        print(f"\nOverpayment = {overpayment}")


def principal():
    a = annuity_payment()
    n = payment_period()
    i = loan_interest()
    p = 0
    if i == 0:
        principal = math.floor(a * n)
        p = 0
        print(f"\nYour loan principal = {principal}!")
    else:
        r = i / (12 * 100)
        principal = a / ((r * ((1 + r) ** n)) / (((1 + r) ** n) - 1))
        principal = math.floor(principal)
        p += principal
        print(f"\nYour loan principal = {principal}!")

    overpayment = int((a * n) - p)

    if overpayment > 0:
        print(f"\nOverpayment = {overpayment}")


def differentiated():
    p = loan_principal()
    n = payment_period()
    i = loan_interest()
    r = (i / (12 * 100))  # Interest Rate

    total_payments = 0

    for m in range(int(n)):
        m = m + 1
        d = (p / n) + r * (p - ((p * (m - 1)) / n))
        d = (math.ceil(d))
        total_payments += d
        print(f"Month {m}: payment is {d}")

    overpayment = int(total_payments - p)

    if overpayment > 0:
        print(f"\nOverpayment = {overpayment}")


if __name__ == '__main__':
    main()
