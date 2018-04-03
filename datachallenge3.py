import pandas as pd
import sqlite3


con = sqlite3.connect('res/Data/FPA_FOD_20170508.sqlite')

names = pd.read_sql("PRAGMA table_info(Fires)", con)
print(names)
del(names)

distinct_vals = pd.read_sql("SELECT DISTINCT * FROM Fires", con)
print(distinct_vals)
del(distinct_vals)

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

important = pd.read_sql("SELECT SOURCE_SYSTEM_TYPE, SOURCE_SYSTEM, NWCG_REPORTING_AGENCY, NWCG_REPORTING_UNIT_NAME, FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS, LATITUDE, LONGITUDE, STATE, COUNTY, FIPS_CODE, FIPS_NAME FROM Fires", con)
print(important.head())
del(important)

location_data = pd.read_sql("SELECT LATITUDE, LONGITUDE, STATE, COUNTY, FIPS_CODE, FIPS_NAME FROM Fires", con)
print(location_data.head())
del(location_data)

fire_data = pd.read_sql("SELECT FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, DISCOVERY_TIME, CONT_DATE, CONT_DOY, CONT_TIME, FIRE_SIZE, FIRE_SIZE_CLASS FROM Fires", con)
print(fire_data.head())
del(fire_data)

report_data = pd.read_sql("SELECT SOURCE_SYSTEM_TYPE, SOURCE_SYSTEM, NWCG_REPORTING_AGENCY, NWCG_REPORTING_UNIT_NAME FROM Fires", con)
print(report_data.head())
del(report_data)

# TODO Chart stats for original data

# TODO One-hot encode

# TODO Perform train and test split

# TODO Train the naive-bayes

# TODO Test the naive-bayes

# TODO Tensorflow softmax train

# TODO Tensorflow softmax test

# TODO Chart train accuracy NB versus SM

# TODO Chart test accuracy NB versus SM
