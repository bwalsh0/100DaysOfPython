import pandas as pd

PATH_INPUT = r''
PATH_REF = r''
PATH_OUTPUT = r''
paths = [PATH_INPUT, PATH_REF]
dataframes = [] # [Input, ref, output]

for filename in paths:
    if filename == '': print("Path empty"); exit(1)
    if filename.rsplit('.', 1)[1] == 'csv':
        dataframes.append(pd.read_csv(filename))
    elif filename.rsplit('.', 1)[1] == 'xlsx':
        dataframes.append(pd.read_excel(filename))
    else:
        print("Unknown file:", filename)
dataframes.append(pd.DataFrame())



########
# Final:
dataframes[-1].to_excel(PATH_OUTPUT)
