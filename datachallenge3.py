import pandas as pd
import sqlite3
# import seaborn as sns
# import matplotlib.pyplot as plt
import urllib
import os.path
from sklearn.naive_bayes import GaussianNB
# import datetime
# import sys


# Automatically inserts values for all present responses in the feature Series
#   into the dicToFill dictionary with the syntax "response|category" along with
#   all the present categories with the syntax "category"
# @param df DataFrame containing all features and corresponding answers, answers
#   must be in the last column, which need bayesian probabilities made for them
#   This DataFrame cannot contain nulls or nans
# @param dicToFill Dictionary to contain all feature response/category combinations
#   with their corresponding probabilities, including the prior probabilities
def buildDFPredictor(df, dicToFill):
    categories = df[df.columns[len(df.columns) - 1]].unique()
    for category in categories:
        dicToFill[category] = (len(df[df[df.columns[len(df.columns)-1]] == category]) / (len(df[df.columns[len(df.columns)-1]])))
    for j in range(len(df.columns) - 1):
        response_counts = df[df.columns[j]].value_counts()
        responses = response_counts.index
        for i,response in enumerate(responses):
            for category in categories:
                dicToFill[str(response)+"|"+str(category)] = len(df[(df[df.columns[j]] == response) & (df[df.columns[len(df.columns) - 1]] == category)]) / int(response_counts.iloc[i])


fname = './res/Data/FPA_FOD_20170508.sqlite'
if os.path.isfile(fname):
    print("data found. not downloading.")
else:
    print("data not found. downloading.")
    url = "https://nofile.io/g/eTXaMMnDOjWfiECxiNW4LjyR43L7o33vAhikYoD8zdkeXzagup2yHUgrKnwltS0S/FPA_FOD_20170508.sqlite/"
    urllib.request.urlretrieve(url, filename=fname)
    print("download complete!")

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

# Get the answers
#answers = pd.read_sql("SELECT STAT_CAUSE_CODE, STAT_CAUSE_DESCR FROM Fires", con)  # Query
#print(answers.head())  # Show
#del(answers)  # Clear memory

# Get the fire info
#fire_data = pd.read_sql("SELECT FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS FROM Fires", con)  # Query
#print(fire_data.head())  # Show
#del(fire_data)  # Clear memory

# Get required fields
#required_data = pd.read_sql("SELECT FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS, STATE, FIPS_CODE, OWNER_DESCR FROM Fires", con)  # Query
required_data = pd.read_sql("SELECT FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS, STATE, COUNTY, FIPS_CODE, STAT_CAUSE_DESCR FROM Fires", con)  # Query
required_data.dropna()
#print(required_data.head())  # Show


# DONE Create durations.
required_data['DUR_FIRE'] = required_data['CONT_DATE'] - required_data['DISCOVERY_DATE']
required_data.dropna()

required_data = required_data[['FIRE_YEAR', 'FIRE_SIZE_CLASS', 'STATE', 'FIPS_CODE', 'DUR_FIRE', 'STAT_CAUSE_DESCR']]

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

required_data_1h = pd.get_dummies(required_data)

print(required_data_1h.head())

# TODO Perform train and test split
train = required_data_1h.sample(frac=.7)
test = required_data_1h.drop(train.index)
w = train.copy()

# TODO Train the naive-bayes

probs = {}
#buildDFPredictor(required_data, probs)
#w_len = len(w)
#probs["Structure"] = sum(w['STAT_CAUSE_DESCR'] == 'Structure') / w_len
#probs["Smoking"] = sum(w['STAT_CAUSE_DESCR'] == 'Smoking') / w_len
#probs["Powerline"] = sum(w['STAT_CAUSE_DESCR'] == 'Powerline') / w_len
#probs["Misc"] = sum(w['STAT_CAUSE_DESCR'] == 'Miscellaneous') / w_len
#probs["NA`"] = sum(w['STAT_CAUSE_DESCR'] == 'Missing/Undefined') / w_len
#probs["Lightening"] = sum(w['STAT_CAUSE_DESCR'] == 'Lightening') / w_len
#probs["Debris_Burning"] = sum(w['STAT_CAUSE_DESCR'] == 'Debris Burning') / w_len
#probs["Campfire"] = sum(w['STAT_CAUSE_DESCR'] == 'Campfire') / w_len
#probs["Equipment_Use"] = sum(w['STAT_CAUSE_DESCR'] == 'Equipment Use') / w_len
#probs["Arson"] = sum(w['STAT_CAUSE_DESCR'] == 'Arson') / w_len
#probs["Children"] = sum(w['STAT_CAUSE_DESCR'] == 'Children') / w_len
#probs["Railroad"] = sum(w['STAT_CAUSE_DESCR'] == 'Railroad') / w_len
#probs["Fireworks"] = sum(w['STAT_CAUSE_DESCR'] == 'Fireworks') / w_len

# TODO Test the naive-bayes


def predict(values):
    print(clf.predict(values))

clf = GaussianNB()
clf.fit(train.sample(frac=.3).as_matrix(), test.sample(frac=.3).as_matrix())
predict(w.sample(frac=.1).as_matrix())
