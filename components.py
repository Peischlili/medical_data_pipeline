from json import JSONEncoder

# Main class used to encapulate all connected graphs
# Drug has 2 native attributes "atccode" and "drug" (name).
# 3 other attributes "pubmed", "clinical_trials" and "clinical_trials"
# are lists of other objects issued from different data sources.
class Drug():
    def __init__(self, atccode, drug):
        self.atccode = atccode
        self.drug = drug
        self.pubmed = []
        self.clinical_trials = []
        self.journal = []
     
    # Add pubmed items mentioned to attribute "pubmed"
    def add_pubmed(self, x):
        self.pubmed.append(x)
    
    # Add clinical trial items mentioned to attribute "clinical_trials"
    def add_ct(self, x):
        self.clinical_trials.append(x)    

    # Add journal items mentioned to attribute "journal"
    def add_journal(self, x):
        self.journal.append(x)
    
    # Retrieve a list of journal names for the drug of interest
    def get_journal_list(self):
        if len(self.journal) != 0:
            j_names = []
            for i, element in enumerate(self.journal): 
                j_names.append(element.name)
            return j_names
        else:
            return []


# Subset object of Drug.pubmed attribute
# Contains information of each mention issued from pubmed       
class Pubmed():
    def __init__(self, pmd_id, title, date, journal):
        self.id = pmd_id
        self.title = title
        self.date_mention = date
        self.journal = journal
    

# Subset object of Drug.clinical_trials attribute
# Contains information of each mention issued from clinical_trials
class ClinicalTrial():
    def __init__(self, nct_id, scientific_title, date, journal):
        self.id = nct_id
        self.scientific_title = scientific_title
        self.date_mention = date
        self.journal = journal
    
 
# Subset object of Drug.journal attribute
# Contains information of each mentioned journal both in pubmed and clinical_trials
# Journal.mentions is a list of mention objects under each single journal
class Journal():
    def __init__(self, name):
        self.name = name
        self.mentions = []
    
    # Add mention items to attribute "mentions"
    def add_mention(self, x):
        self.mentions.append(x)


# Subset object of Drug.journal.mentions attribute
class Mention():
    def __init__(self, source, source_id, date):
        self.source = source
        self.source_id = source_id
        self.date_mention = date
        

# Subclass of JSONEncoder: used to generate .json file
class DrugEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

        
