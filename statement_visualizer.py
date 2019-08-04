import csv
import matplotlib.pyplot as plt

i = 0
date, expenses = [], []
labelExpense = [{"Label": "", "Amount": 0}]

input_path = r'\statement.CSV'
output_path = r'\statement.CSV'


def main():
    with open(input_path) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row.get('Type') == 'CHASE_TO_PARTNERFI' or \
                    row.get('Type') == 'QUICKPAY_DEBIT' or \
                    row.get('Type') == 'ACH_DEBIT':
                continue

            amt = float(row.get('Amount'))

            if amt is not None and amt < 0:
                amt *= -1.00
                label = row.get('Description')[:5]
                # day = row.get('Posting Date')

                # Expenses over time (per day)
                # if len(date) > 0 and day == date[-1]:
                #     expenses[-1] += amt
                # else:
                #     expenses.append(amt)
                #     date.append(day)

                if len(labelExpense) > 0 and label == labelExpense[-1]["Label"]:
                    labelExpense[-1]["Amount"] += amt
                else:
                    labelExpense.append({"Label": label, "Amount": amt})

    labelExpense.sort(key=lambda l:l["Label"])

    # with open(output_path, 'w+') as csvout:
    #     writer = csv.writer(csvout)
    #     writer.writerows(labelExpense)

    labelList = []
    expenseList = []

    for i in labelExpense:
        labelList.append(i["Label"])
        expenseList.append(i["Amount"])

    plt.plot(labelList, expenseList)
    plt.ylabel('Expense')
    plt.xlabel('Label')
    plt.show()

    exit()


main()
