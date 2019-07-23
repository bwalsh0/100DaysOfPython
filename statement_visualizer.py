import csv
import matplotlib.pyplot as plt

i = 0
date, expenses = [], []
labels, labelExpense = [], []


def main():
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
                label = row.get('Label')
                day = row.get('Posting Date')

                # Expenses over time (per day)
                # if len(date) > 0 and day == date[-1]:
                #     expenses[-1] += amt
                # else:
                #     expenses.append(amt)
                #     date.append(day)

                if len(labels) > 0 and label == labels[-1]:
                    labelExpense[-1] += amt
                else:
                    labelExpense.append(amt)
                    labels.append(label)

    with open('statement_OUTPUT.CSV', 'w+') as csvout:
        writer = csv.writer(csvout)
        writer.writerows(zip(labels, labelExpense))

    plt.plot(labels, labelExpense)
    plt.ylabel('Expense')
    plt.xlabel('Date')
    plt.show()

    exit()


main()
