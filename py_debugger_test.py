from os import listdir
from os.path import isfile, join

PATH = r'C:\Users\Bryan Walsh\Documents\GitHub\tensor_new'

files = [file for file in listdir(PATH) if isfile(join(PATH, file))]

for i in files:
    print(i.rsplit('.', 1)[1])

exit(0)

# {
#     "version": "0.2.0",
#     "configurations": [
        
#         {
#             "name": "Python: Current File",
#             "type": "python",
#             "request": "launch",
#             "program": "${file}",
#             "console": "integratedTerminal"
#         }
#     ]
# }
