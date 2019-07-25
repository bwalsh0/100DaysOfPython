outerDict = {}
elemId = {}

# For a specific-case project

with open(r'dict_demo.txt', 'r') as txtFile:
    for line in txtFile.readlines():
        uid = line.partition("=")[2][:3]
        elemId = {uid: {}}
        elemId[uid].update(dict(s.split('=',1) for s in line[10:].strip().split(',',1)))
        outerDict.update(elemId)

        # future:
        #
        # each file line into dict
        # sort by volume counter
        # discard counters below threshold
        # turn remaining into a tree {a{1,...8}} using partition()

print(outerDict)
