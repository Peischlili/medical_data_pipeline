import pandas as pd
import json


# Relative paths of pubmed files to be compiled
pubmed1 = "data/pubmed.csv"
pubmed2 = "data/pubmed.json"

# Load csv file
df_pubmed1 = pd.read_csv(pubmed1, sep=",", encoding="utf-8")

# Load, reformat json file and save newly modified json
with open(pubmed2) as f:
    lines = f.readlines()
f.close()

# Remove "," present after the last dictionary before closing square bracket
if lines[-2] == '  },\n' and lines[-1] == ']':
    lines[-2] ='  }\n'

# Save modified json file to be used in upcoming compilation
pubmed2_new = "data/pubmed_bis.json"
with open(pubmed2_new, "w") as f:
    f.writelines(lines)
f.close()

# Open newly created json file and load to dataframe
with open(pubmed2_new) as f:
    data = f.read()
    pubmed2_array = json.loads(data)
f.close()

df_pubmed2 = pd.DataFrame(pubmed2_array)

# Concatenate 2 pubmed files (.csv and .json) ans save to a single csv file
df_pubmed = pd.concat([df_pubmed1, df_pubmed2], axis=0,ignore_index=True)
df_pubmed['id'] =  df_pubmed['id'].map(lambda x: str(x))
pubmed_restit = "data/pubmed_restit.csv"
df_pubmed.to_csv(pubmed_restit, index=False)