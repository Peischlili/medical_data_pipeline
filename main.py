import json
import sys
from components import DrugEncoder, Pubmed, ClinicalTrial
from processing_fct import load_n_clean_ct, load_n_clean_pubmed, create_drugs_from_list
from processing_fct import filter_mentioned, create_jounal_mentions


# Relative path of input files
drugs = "data/drugs.csv"
pubmed = "data/pubmed_restit.csv"
ct = "data/clinical_trials.csv"

# Relative path of output json file
output_f = 'data/complete_data.json'


def main():
    global drugs, pubmed, ct, output_f
    # Load files and process data cleaning
    df_ct = load_n_clean_ct(ct)
    df_pubmed = load_n_clean_pubmed(pubmed)
    
    # Load drugs.csv, process data cleaning and create a collection of Drug objects
    list_drugs = create_drugs_from_list(drugs)
    
    # Iterate over collection of Drug objects to establish connections to pubmed and ct data sources
    for drug in list_drugs:
        # Filter pubmed data containing drug
        df_temp = filter_mentioned(df_pubmed, drug, 'title')
        
        # Iterate over pubmed dataframe
        for ind in df_temp.index:
            # create pubmed objects and add them to Drug objects
            p = Pubmed(str(df_temp['id'][ind]), str(df_temp['title'][ind]), str(df_temp['date'][ind]), str(df_temp['journal'][ind]))
            drug.add_pubmed(p)
            
            # create journal object if non existant, and add mentions to associated journals
            create_jounal_mentions(df_temp, ind, drug, 'pubmed')
         
        # Filter clinical trials data containing drug
        df_temp = filter_mentioned(df_ct, drug, 'scientific_title')
        
        # Iterate over clinical trails dataframe 
        for ind in df_temp.index:
        # create ct object: n mentioned ct have n objects
        # add those ct objects to Drug object
            ct = ClinicalTrial(str(df_temp['id'][ind]), str(df_temp['scientific_title'][ind]), str(df_temp['date'][ind]), str(df_temp['journal'][ind]))
            drug.add_ct(ct)
            
            # create journal object if non existant, and add mentions to associated journals
            create_jounal_mentions(df_temp, ind, drug, 'clinical trials')
        
    # Output collection of drugs "list_drugs" to .json file
    with open(output_f, 'w') as outfile:
        json.dump(list_drugs, outfile, indent=4, cls=DrugEncoder, ensure_ascii=False)


if __name__ == "__main__":
    sys.exit(main())
