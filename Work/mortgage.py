# mortgage.py
#
# Exercise 1.7

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = int(input('start month '))
extra_payment_end_month = int(input('end month '))
extra_payment = int(input('extra payment '))

while principal > 0.01:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = 2684.11 + extra_payment
    else:
        payment = 2684.11
    if payment > principal:
        payment = principal * (1+rate/12)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, round(total_paid,2), round(principal,2))
    month += 1

print(f'Total Paid ${total_paid:,.2f}, Month {month-1}, Last Payment ${payment:,.2f}')