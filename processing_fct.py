import re
import pandas as pd
from components import Drug, Journal, Mention


# Data cleaning function to process clinical_trails.csv
def load_n_clean_ct(ct_path):
    df_ct = pd.read_csv(ct_path, sep=",", encoding="utf-8")
    # Remove duplicates
    df_ct.drop_duplicates(inplace=True)
    # Groupby combination and aggregate lines to complete information
    df_ct = df_ct.groupby(['scientific_title','date']).agg(lambda x: x.dropna(axis=0)).reset_index()
    # Change data types (specially for 'date' column)
    df_ct = df_ct.astype({
        'id': 'str',
        'scientific_title': 'str',
        'date': 'datetime64',
        'journal': 'str'
    })
    return df_ct


# Data cleaning function to process pubmed_restit.csv
def load_n_clean_pubmed(pubmed_path):
    df_pubmed = pd.read_csv(pubmed_path, sep=",", encoding="utf-8")
    # Remove duplicates
    df_pubmed.dropna(inplace=True)
    # Change data types (specially for 'date' column) and cast 'id' to string
    df_pubmed = df_pubmed.astype({
        'id': 'int32',
        'title': 'str',
        'date': 'datetime64',
        'journal': 'str'
    })
    df_pubmed['id'] = df_pubmed['id'].map(lambda x: str(x))
    return df_pubmed


# Function to create Drug objects from drugs.csv file
# list_drugs: collection of Drug objects
def create_drugs_from_list(drugs_path):
    df_drugs = pd.read_csv(drugs_path, sep=",", encoding="utf-8")
    list_drugs = []
    for ind in df_drugs.index:
        d = Drug(str(df_drugs['atccode'][ind]), str(df_drugs['drug'][ind]))
        list_drugs.append(d)
    return list_drugs


# Take a Pubmed or clinical_trials dataframe and return subset of records
# that mentioned durg of interest
# drug: a Drug object; title_column: column name containing titles
def filter_mentioned(df_temp, drug, title_column):
    # create serie to process text formatting: remove any none digit/letter/underscore
    # and create for each pubmed item a title collection of individual words 
    title_list = df_temp[title_column].map(lambda x: re.sub(r"\W+", " ", x).upper().split())
    
    # l: list of bool whether contains drug name in title
    # inject l into newly named column called "containsDrug"
    l = []
    for title in title_list:
        l.append(str(drug.drug) in title)
    df_temp['containsDrug'] = l
    
    # filter records that contains drug in question
    df_filter = df_temp[df_temp['containsDrug']]
    return df_filter


# Given a filtered dataframe (pubmed or clinical_trials), create journal and mention objects
# and update Drug objects
# drug: a Drug object; ind: one of df_filter.index; source: string label such as 'pubmed' or 'clinical trials'
def create_jounal_mentions(df_filter, ind, drug, source):
    # create journal object if non existant for the drug of interest
    j_name = str(df_filter['journal'][ind])
    # if Drug.journal not empty, check if journal name exists before creating new journal object
    # if existant, skip this step
    if (len(drug.journal) > 0): 
        j_list = drug.get_journal_list()
        if j_name not in j_list:
            j_object = Journal(j_name)
            drug.add_journal(j_object)
    else:
        j_object = Journal(j_name)
        drug.add_journal(j_object)
            
    # locate concerned journal index and add mentions
    # get updated list 
    j_list = drug.get_journal_list()
    j_index = j_list.index(j_name)
    # access to journal object and add mention from pubmed
    m = Mention(source, str(df_filter['id'][ind]), str(df_filter['date'][ind]))
    drug.journal[j_index].add_mention(m)