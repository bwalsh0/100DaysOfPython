# For a specific-case project

CONST_ITEM_TYPES = ['itemA', 'itemB', 'itemC', 'itemD', 'itemE', 'itemF', 'itemG', 'itemH']
unsortedList, sortedList = [], []


def sortList(sortedList):
    # Sort all lists in outerList by the 2nd value in the tuple element
    sortedList.sort(key=lambda l: l[-1][1], reverse=True)
    print(sortedList)


def parseFile():
    # 5000 items, 46ms
    with open(r'dict_demo.txt', 'r') as data:
        for line in data.readlines():
            lineSplit = line.partition('.txt:')
            fileId = lineSplit[0]
            line = lineSplit[2]

            line = line.replace(' ', ',', 1).replace(' ', '=', 1).strip()
            listItem = [s.split('=')[1] for s in line.split(',')]
            listItem.insert(0, fileId)
            unsortedList.append(listItem)
    data.close()

    for index, innerList in enumerate(unsortedList):
        # Add item indentifier to value as tuple (itemN, 8)
        innerList[-1] = (CONST_ITEM_TYPES[index % 8], innerList[-1])

    sortList(unsortedList)


def main():
    parseFile()


main()
