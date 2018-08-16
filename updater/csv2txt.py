#encoding: iso-8859-1

import os
import pandas # pip install pandas


# SETUP
pwd : str = os.getcwd()
data = pandas.read_csv(pwd + "/in.csv", sep=',', encoding='iso-8859-1')

model = open(pwd + "/model.txt", mode='r', encoding='iso-8859-1')
output = open(pwd + "/out.txt", mode='w', encoding='iso-8859-1')

column_field : str = '#'


# PROCESSING
model.seek(0, 2)
model_end = model.tell()
print("Model file has %d characters." % model_end)

rows : int = len(data.index)
print("Input csv file has %d rows..." % rows)

for i in range(0, rows):
    print("..." + data.iloc[i, 1])

    cursor: int = 0
    while (cursor < model_end):
        model.seek(cursor, 0)
        ch : str = model.read(1) # one char at a time

        if ch == column_field:
            j = int(model.read(1)) # read the column number next to the column_field
            cursor += 1
            output.write(str(data.iloc[i, j]))
        else:
            output.write(ch)

        cursor += 1 # moves the cursor


# END
output.close()
model.close()
print("Done!")
