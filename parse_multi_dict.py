outer = []

# For a specific-case project
# Both cases have identical results with different data structures and runtimes

with open(r'dict_demo.txt', 'r') as txtFile:
    # 5000 lines, 48 ms
    for line in txtFile.readlines():
        line = line.replace(' ', ',', 1).replace(' ', '=', 1).strip()
        outer.append(dict(s.split('=') for s in line.split(',')))
    outer.sort(key=lambda l: int(list(l.values())[3]), reverse=True)

    # 5000 lines, 36 ms
    # for line in txtFile.readlines():
    #     line = line.replace(' ', ',', 1).replace(' ', '=', 1).strip()
    #     outer.append([s.partition('=')[2] for s in line.split(',', 2)])
    #
    # for i in outer:
    #     part = i[2].partition(',')
    #     part2 = part[2].partition('=')
    #     i[2] = part[0]
    #     i.append((part2[0], int(part2[2])))
    #
    # outer.sort(key=lambda l: l[3][1], reverse=True)

print(outer)
# for i in outer:
#     print(i)
