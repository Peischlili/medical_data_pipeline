import json
import pandas as pd

# Relative path of input file
data_file = "data/complete_data.json"
# Relative path of output file
outfile = "data/analyse_ad_hoc.csv"

# Load json file
with open(data_file, "r") as f:
    data = json.loads(f.read())
f.close()

# Create dataframe containing following information: atccode, drug (name), journal
df_records = pd.DataFrame()
for i in data:
    atccode = i['atccode']
    drug = i['drug']
    for journal in i['journal']:
        j_name = journal['name']
        #print(atccode, drug, j_name)
        d = {'atccode': [atccode], 'drug': [drug], 'journal': [j_name]}
        record = pd.DataFrame(data=d, dtype='str')
        df_records = pd.concat([df_records, record], ignore_index=True)

# Retrieve information to answer the following question:
# "Name of the journal that mentions the largest number of different drugs"
df_result = df_records.groupby(by=["journal"]).count().sort_values('drug', ascending=False)
df_result.to_csv(outfile)