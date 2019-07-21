import csv
import numpy as np

# Remove semi-duplicate, but non-identical data entries to aid in pre-processing datasets. 

date, transactions = [], []
i = 0

with open(r'dataset_stmt.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        description = row.get('Desc')
        if i > 0:
            keyword = transactions[-1]
            if keyword[0:3] != description[0:3]:
                transactions.append(description)
                print(description)
        else:
            transactions.append(description)
        i += 1

np.savetxt('dataset_stmt_CLEAN.csv', transactions, delimiter=',')
exit()
