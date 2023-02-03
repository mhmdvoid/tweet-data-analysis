import csv
import math
import random

lables = ["الاعاشة والتغذية", 'السكن', 'التنظيم', 'التنظيم', 'المواصلات', 'الصحة', "العبادة", 'العبادة', 'حملات الحج', 'الطقس', 'التعامل',
          'خدمات الدعم اللوجستي', 'الامن']  # place your lables to write them randomly.


# this will label your data in specific column. Actually this is for our use. You could take it and play around with it to customize it.
whole_data = []
with open("LableFile.csv") as csv_file:
    for row in csv.reader(csv_file, delimiter=','):
        col = 0
        pairs = ()
        for column in row:
            # col_val = column
            col += 1
            if col == 2:
                # we're in lable_field;
                print(column)
                if column == '':
                    column = random.choice(lables)
            pairs = pairs + (column,)
        whole_data.append(pairs)

print(whole_data)
writer = csv.writer(open("FullLabel.csv", 'w'))
writer.writerows(whole_data)
# for data in whole_data:
#     writer.writerow([data])
# df = pd.DataFrame(whole_data)
# df.drop_duplicates()
# df.to_csv("FullLabel.csv")
