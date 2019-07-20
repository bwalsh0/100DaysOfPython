import csv
import matplotlib.pyplot as plt

i = 0
date, expenses = [], []

with open(r'statement.CSV') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        if row.get('Type') == 'CHASE_TO_PARTNERFI' or \
                row.get('Type') == 'QUICKPAY_DEBIT' or \
                row.get('Type') == 'ACH_DEBIT':
            continue
        amt = float(row.get('Amount'))
        if amt is not None and amt < 0:
            amt *= -1.00
            day = row.get('Posting Date')
            if len(date) > 0 and day == date[-1]:
                expenses[-1] += amt
            else:
                expenses.append(amt)
                date.append(day)
        # i += 1
        # if i == 100:
        #     csvfile.close
        #     break
    print(date, expenses)

plt.plot(date, expenses, scalex=True, scaley=True)

# hist = plt.plot(80, y, 'r--', linewidth=2)
plt.grid(True)
# plt.axis([0, 730, 0, 2000])
plt.ylabel('Expense')
plt.xlabel('Date')
# plt.text(75, 1600, 'bin=3.5days')
plt.show()
