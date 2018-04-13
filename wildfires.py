import pandas as pd
import sqlite3
import urllib
import os.path
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

# Automatically inserts values for all present responses in the feature Series
#   into the dicToFill dictionary with the syntax "response|category" along with
#   all the present categories with the syntax "category"
# @param df DataFrame containing all features and corresponding answers, answers
#   must be in the last column, which need bayesian probabilities made for them
#   This DataFrame cannot contain nulls or nans
# @param dicToFill Dictionary to contain all feature response/category combinations
#   with their corresponding probabilities, including the prior probabilities
#def buildDFPredictor(df, dicToFill):
#    categories = df[df.columns[len(df.columns) - 1]].unique()
#    for category in categories:
#        dicToFill[category] = (len(df[df[df.columns[len(df.columns)-1]] == category]) / (len(df[df.columns[len(df.columns)-1]])))
#    for j in range(len(df.columns) - 1):
#        response_counts = df[df.columns[j]].value_counts()
#        responses = response_counts.index
#        for i,response in enumerate(responses):
#            for category in categories:
#                dicToFill[str(response)+"|"+str(category)] = len(df[(df[df.columns[j]] == response) & (df[df.columns[len(df.columns) - 1]] == category)]) / int(response_counts.iloc[i])


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

# Get the answers
#answers = pd.read_sql("SELECT STAT_CAUSE_CODE, STAT_CAUSE_DESCR FROM Fires", con)  # Query
#print(answers.head())  # Show
#del(answers)  # Clear memory

# Get required fields
required_data = pd.read_sql("SELECT FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS, STATE, COUNTY, FIPS_CODE, STAT_CAUSE_DESCR FROM Fires", con)  # Query
required_data.dropna()

# DONE Create durations.
required_data['DUR_FIRE'] = required_data['CONT_DATE'] - required_data['DISCOVERY_DATE']
required_data.dropna()

required_data = required_data[['FIRE_YEAR', 'FIRE_SIZE_CLASS', 'STATE', 'DUR_FIRE', 'STAT_CAUSE_DESCR']]

# DONE One-hot encode
required_data_1h = pd.get_dummies(required_data[['FIRE_YEAR', 'FIRE_SIZE_CLASS', 'STATE', 'DUR_FIRE']])

# DONE Perform train and test split
features_train, features_test, target_train, target_test = train_test_split(required_data_1h, required_data["STAT_CAUSE_DESCR"], test_size=.3, random_state=100)





# TODO Train the naive-bayes

# TODO Test the naive-bayes
def predict(values):
    return clf.predict(values)

clf = GaussianNB()
clf.fit(features_train, target_train)
target_pred = predict(features_test)
print(sum(target_pred == target_test) / len(features_test))