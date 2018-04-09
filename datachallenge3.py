import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import urllib
import os.path
import datetime
import numpy as np
import importlib

nb = importlib.import_module("./res/HybridNaiveBayes/nb.py")
distributions = importlib.import_module("./res/HybridNaiveBayes/distributions.py")

fname = './res/Data/FPA_FOD_20170508.sqlite'
if os.path.isfile(fname):
    print("data found. not downloading.")
else:
    print("data not found. downloading.")
    url = "https://nofile.io/g/eTXaMMnDOjWfiECxiNW4LjyR43L7o33vAhikYoD8zdkeXzagup2yHUgrKnwltS0S/FPA_FOD_20170508.sqlite/"
    urllib.request.urlretrieve(url, filename=fname)
    print ("download complete!")

#Establish database connection
con = sqlite3.connect(fname)
#cr = con.cursor()

# Get all column names for table Fires
#names = pd.read_sql("PRAGMA table_info(Fires)", con)  # Query
#print(names)  # Show
#del(names)  # Clear memory

# Get the distinct values for all columns in Fires
#distinct_vals = pd.read_sql("SELECT DISTINCT * FROM Fires", con)  # Query
#print(distinct_vals)  # Show
#del(distinct_vals)  # Clear memory


"""
format:
COLUMN WORTH
    COLUMN TYPE
        COLUMN NAME
            UNIQUE VALUES

Important Columns:
    Data:
        SOURCE_SYSTEM_TYPE
            FED
            NONFED
            INTERAGCY
        SOURCE_SYSTEM
            FS-FIRESTAT
            DOI-WFMI
            FWS-FMIS
            FA-NFIRS
            ST-NASF
            ST-AZAZS
            ST-MOMOS
            IA-AKACC
            ST-MTMTS
            ST-SCSCS
            ST-COCOS
            ST-MEMES
            ST-ORORS
            ST-MSMSS
            ST-NMNMS
            ST-SDSDS
            ST-UTUTS
            ST-WAWAS
            ST-WYWYS
            ST-OKOKS
            ST-WIWIS
            ST-MIMIS
            ST-KYKYS
            ST-ALALS
            ST-ARARS
            ST-GAGAS
            ST-LALAS
            ST-TNTNS
            ST-VAVAS
            ST-FLFLS
            ST-NCNCS
            IA-ICS209
            ST-CACDF
            ST-CTCTS
            ST-NENES
            ST-TXTXS
            IA-PRIITF
            IA-HIWMO
        NWCG_REPORTING_AGENCY
            FS
            BIA
            TRIBE
            BLM
            NPS
            BOR
            FWS
            ST/C&L
            DOD
            IA
            DOE
        NWCG_REPORTING_UNIT_NAME
            County Names
            University Names
            Firehouse Names
        FIRE_YEAR
            Years 1980?-2017
        DISCOVERY_DATE
            Date 1980?-2017
        DISCOVERY_DOY
            Date 1980?-2017
        DISCOVERY_TIME
            Timevalue
        CONT_DATE
            Date 1980?-2017
        CONT_DOY
            Date 1980?-2017
        CONT_TIME
            Timevalue
        FIRE_SIZE
            FLOAT
        FIRE_SIZE_CLASS
            A-E
        LATITUDE
            Latitude Coordinate Decimal Degrees
        LONGITUDE
            Longitude Coordinate Decimal Degrees
        STATE
            1 of 50 US States
        COUNTY
            County Names
        FIPS_CODE
            A FIPS Code
        FIPS_NAME
            A FIPS Name

    Answers:
        STAT_CAUSE_CODE
            Integer Index
        STAT_CAUSE_DESCR
            Answer
"""

# Get all the important columns
#important = pd.read_sql("SELECT SOURCE_SYSTEM_TYPE, SOURCE_SYSTEM, NWCG_REPORTING_AGENCY, NWCG_REPORTING_UNIT_NAME, FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS, LATITUDE, LONGITUDE, STATE, COUNTY, FIPS_CODE, FIPS_NAME FROM Fires", con)  # Query
#print(important.head())  # Show
#del(important)  # Clear memory


# Get the answers
#answers = pd.read_sql("SELECT STAT_CAUSE_CODE, STAT_CAUSE_DESCR FROM Fires", con)  # Query
#print(answers.head())  # Show
#del(answers)  # Clear memory


# Get the location info
#location_data = pd.read_sql("SELECT LATITUDE, LONGITUDE, STATE, COUNTY, FIPS_CODE, FIPS_NAME FROM Fires", con)  # Query
#print(location_data.head())  # Show
#del(location_data)  # Clear memory


# Get the fire info
#fire_data = pd.read_sql("SELECT FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS FROM Fires", con)  # Query
#print(fire_data.head())  # Show
#del(fire_data)  # Clear memory


# Get the reporting info
#report_data = pd.read_sql("SELECT SOURCE_SYSTEM_TYPE, SOURCE_SYSTEM, NWCG_REPORTING_AGENCY, NWCG_REPORTING_UNIT_NAME FROM Fires", con)  # Query
#print(report_data.head())  # Show
#del(report_data)  # Clear memory


# Get required fields
#required_data = pd.read_sql("SELECT FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS, STATE, FIPS_CODE, OWNER_DESCR FROM Fires", con)  # Query
required_data = pd.read_sql("SELECT FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS, STATE, COUNTY, FIPS_CODE, FIPS_NAME, STAT_CAUSE_DESCR FROM Fires", con)  # Query
required_data.dropna()
#print(required_data.head())  # Show

# TODO Clean data

# Shows null counts
#print(required_data.CONT_DATE.isnull().value_counts())
#print(required_data.DISCOVERY_DATE.isnull().value_counts())
#print(required_data.DISCOVERY_DOY.isnull().value_counts())
#print(required_data.DISCOVERY_TIME.isnull().value_counts())
#print(required_data.CONT_DOY.isnull().value_counts())
#print(required_data.CONT_TIME.isnull().value_counts())
#print(required_data.FIRE_SIZE.isnull().value_counts())
#print(required_data.FIRE_SIZE_CLASS.isnull().value_counts())
#print(required_data.STATE.isnull().value_counts())
#print(required_data.COUNTY.isnull().value_counts())
#print(required_data.FIPS_CODE.isnull().value_counts())
#print(required_data.FIPS_NAME.isnull().value_counts())
#county, fips_code, fips_name all have the same number of nulls 678148, suspect these are not rows we want
#discovery_time, cont_doy, cont_date, cont_time are all 50% nulls
#The rest of the columns have 0 nulls

#required_data['FIPS_CODE'] = required_data['FIPS_CODE'].where(required_data['FIPS_CODE'] == '40', '040')

# TODO Convert dates to durations (num days)
required_data['DUR_FIRE'] = required_data['CONT_DATE'] - required_data['DISCOVERY_DATE']
required_data.dropna()

#del(required_data)  # KEEP THIS DATA IN FINAL VERSION
# TODO Chart stats for original data

# Create size/year chart
#sns.regplot(x='DUR_FIRE', y='FIRE_SIZE', data=required_data)  # Create chart
#plt.title('Fires Sizes / Duration')
#plt.xlabel('Duration')
#plt.ylabel('Fire sizes')
#plt.show()
#del(year_size) # Clear memory

# TODO One-hot encode

# TODO Perform train and test split
train = required_data.sample(frac=.7)
test = required_data.drop(train.index)
w = train.copy()

# TODO Train the naive-bayes
probs = {}
w_len = len(w)
probs["Structure"] = sum(w['STAT_CAUSE_DESCR'] == 'Structure') / w_len
probs["Smoking"] = sum(w['STAT_CAUSE_DESCR'] == 'Smoking') / w_len
probs["Powerline"] = sum(w['STAT_CAUSE_DESCR'] == 'Powerline') / w_len
probs["Misc"] = sum(w['STAT_CAUSE_DESCR'] == 'Miscellaneous') / w_len
probs["NA"] = sum(w['STAT_CAUSE_DESCR'] == 'Missing/Undefined') / w_len
probs["Lightening"] = sum(w['STAT_CAUSE_DESCR'] == 'Lightening') / w_len
probs["Misc"] = sum(w['STAT_CAUSE_DESCR'] == 'Miscellaneous') / w_len
probs["Debris_Burning"] = sum(w['STAT_CAUSE_DESCR'] == 'Debris Burning') / w_len
probs["Campfire"] = sum(w['STAT_CAUSE_DESCR'] == 'Campfire') / w_len
probs["Equipment_Use"] = sum(w['STAT_CAUSE_DESCR'] == 'Equipment Use') / w_len
probs["Arson"] = sum(w['STAT_CAUSE_DESCR'] == 'Arson') / w_len
probs["Children"] = sum(w['STAT_CAUSE_DESCR'] == 'Children') / w_len
probs["Railroad"] = sum(w['STAT_CAUSE_DESCR'] == 'Railroad') / w_len
probs["Fireworks"] = sum(w['STAT_CAUSE_DESCR'] == 'Fireworks') / w_len
# TODO Test the naive-bayes


def featurizer(data_point):
    return [
        # Bucketed and therefore categorical:
        nb.Feature("Checking account status", distributions.Multinomial, data_point[0]),

        # Continuous and probably follows a power law distribution:
        nb.Feature("Duration in months", distributions.Exponential, float(data_point[1])),

        # Categorical:
        nb.Feature("Credit history", distributions.Multinomial, data_point[2]),

        # Categorical:
        nb.Feature("Purpose", distributions.Multinomial, data_point[3]),

        # Continuous and probably conforms to an approximate power law distribution:
        nb.Feature("Credit amount", distributions.Gaussian, float(data_point[4])),

        # Bucketed and therefore categorical:
        nb.Feature("Savings account status", distributions.Multinomial, data_point[5]),

        # Bucketed and therefore categorical:
        nb.Feature("Unemployment duration", distributions.Multinomial, data_point[6]),

        # Continuous and probably conforms to an approximate power law distribution:
        nb.Feature("Installment rate", distributions.Gaussian, float(data_point[7])),

        # Categorical:
        nb.Feature("Personal status", distributions.Multinomial, data_point[8]),

        # Categorical:
        nb.Feature("Other debtors", distributions.Multinomial, data_point[9]),

        # Continuous and probably conforms to an approximate power law distribution:
        nb.Feature("Present residence", distributions.Exponential, float(data_point[10])),

        # Categorical:
        nb.Feature("Property status", distributions.Multinomial, data_point[11]),

        # Continuous and probably conforms to an approximate power law distribution:
        nb.Feature("Age", distributions.Gaussian, float(data_point[12])),

        # Categorical:
        nb.Feature("Other installment plans", distributions.Multinomial, data_point[13]),

        # Categorical:
        nb.Feature("Housing", distributions.Multinomial, data_point[14]),

        # Continuous and probably conforms to an approximate power law distribution:
        nb.Feature("Number of credit cards", distributions.Exponential, float(data_point[15])),

        # Categorical:
        nb.Feature("Job", distributions.Multinomial, data_point[16]),

        # Continuous and probably conforms to an approximate power law distribution:
        nb.Feature("Number of people liable", distributions.Exponential, float(data_point[17])),

        # Categorical:
        nb.Feature("Telephone", distributions.Multinomial, data_point[18]),

        # Categorical:
        nb.Feature("Foreign worker", distributions.Multinomial, data_point[19])
    ]


def predict():
    classifier = nb.NaiveBayesClassifier(featurizer)
    classifier.train(train, train["STAT_CAUSE_DESCR"])
    print "Accuracy = %s" % classifier.accuracy(train, test["STAT_CAUSE_DESCR"])


predict()
