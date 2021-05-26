import math
import sys
import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=("""This loan calculator can compute the following. \
\n-----------------------------------------------
  - Your loans annuity monthly payment amount.
  - Your number of monthly payments due.
  - Your loan principal.
  - Your differentiated payments."""))

parser.add_argument("-t", "--type",
                    help="You need to choose from either option: \
                    - annuity: for annuity options. \
                    - diff: for the differentiated payments.")

parser.add_argument("-l", "--principal", type=float,
                    help="The amount being borrowed.")

parser.add_argument("-p", "--payment", type=float,
                    help="The monthly payment due on the loan.")

parser.add_argument("-n", "--periods", type=float,
                    help="The time between the first payment on a loan and \
                    its maturity.")

parser.add_argument("-i", "--interest", type=float,
                    help="The amount charged on top of the principal.")

args = parser.parse_args()

if args.type is None or args.type not in ["annuity", "diff"]:
    print("Incorrect parameters")
    exit()
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
    exit()
elif len(sys.argv) != 5:
    print("Incorrect parameters")
    exit()
elif args.interest is None:
    print("Incorrect parameters")
    exit()
else:
    for i in sys.argv[2:]:
        if float(i.split("=")[-1]) < 0:
            print("Incorrect parameters")
            exit()

# Calculates loan differentiated payments and overpayment.
if args.type == "diff":
    p = args.principal
    n = args.periods
    i = args.interest
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

# Calculates monthly payments.
if args.type == "annuity":
    if args.principal and args.payment and args.interest:
        loan = args.principal
        payment = args.payment
        interest = args.interest
        y = 0
        m = 0
        rate = interest / (12 * 100)
        base = payment / (payment - rate * loan)
        months = math.log(base, 1 + rate)
        y = math.floor(months / 12)
        m = math.ceil(months % 12)
        if m == 12:
            y += 1
            m = 0

        if y >= 2 and m >= 2:
            print(f"It will take {y} years and {m} months to repay this \
            loan!")
        elif y == 1 and m >= 2:
            print(f"It will take {y} year and {m} months to repay this \
            loan!")
        elif y >= 2 and m == 1:
            print(f"It will take {y} years and {m} month to repay this \
            loan!")
        elif y == 0 and m >= 2:
            print(f"It will take {m} months to repay this loan!")
        elif y == 0 and m == 1:
            print(f"It will take {m} month to repay this loan!")
        elif y >= 2 and m == 0:
            print(f"It will take {y} years to repay this loan!")
        elif y == 1 and m == 0:
            print(f"It will take {y} year to repay this loan!")

        total_payments = int(payment * ((y * 12) + m))
        overpayment = int(total_payments - loan)

        if overpayment > 0:
            print(f"Overpayment = {overpayment}")

# Calculates loan annuity.
    elif args.principal and args.periods and args.interest:
        loan = args.principal
        n = args.periods
        i = args.interest

        total_payments = 0

        r = i / (12 * 100)
        annuity = loan * ((r * ((1 + r) ** n)) / (((1 + r) ** n) - 1))
        annuity = math.ceil(annuity)
        total_payments += annuity * n

        print(f"Your annuity payment = {annuity}!")

        overpayment = int(total_payments - loan)

        if overpayment > 0:
            print(f"Overpayment = {overpayment}")

# Calculates loan principal.
    elif args.payment and args.periods and args.interest:
        a = args.payment
        n = args.periods
        i = args.interest
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
            print(f"Your loan principal = {principal}!")

        overpayment = int((a * n) - p)

        if overpayment > 0:
            print(f"Overpayment = {overpayment}")
