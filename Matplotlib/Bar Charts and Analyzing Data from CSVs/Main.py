from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

plt.style.use("fivethirtyeight")

# with open('Data-science/Matplotlib/Bar Charts and Analyzing Data from CSVs/data.csv') as csv_file:
#         csv_reader = csv.DictReader(csv_file)

#     row = next(csv_reader)
#     print(row['LanguagesWorkedWith'].split(';'))
#     print(row)


        # language_counter = Counter()

        # for row in csv_reader:
        #         language_counter.update(row["LanguagesWorkedWith"].split(";"))

# for item in language_counter.most_common(30):
#         languages.append(item[0])
#         popularity.append(item[1])

# print(language_counter)


# ----------------------------------------------------------------------------------------------------------------------

data = pd.read_csv(
    "Data-science/Matplotlib/Bar Charts and Analyzing Data from CSVs/data.csv")

language_counter = Counter()

ids = data['Responder_id']
languages = data['LanguagesWorkedWith']

for response in languages:
        language_counter.update(response.split(";"))


languages = []
popularity = []

for item in language_counter.most_common(30):
        languages.append(item[0])
        popularity.append(item[1])


languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming languages")
plt.xlabel("Number of users")

plt.tight_layout()

plt.savefig("plot.png")
plt.plot()
plt.show()












# ==================================================================================================================================
# import csv
# import pandas as pd
# # url = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/02-BarCharts/data.csv'
# # data = pd.read_csv(url, sep=",")  # use sep="," for coma separation.


# with open('data.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(
#         employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
# #     employee_writer.writerows(data)
