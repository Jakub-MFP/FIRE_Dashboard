import pandas as pd
from pandas import DataFrame
import json
import requests
import sqlite3
import time
import datetime
from datetime import datetime as dt


###########################################################################
### CONNECT TO SQLITE DATABASE ############################################
conn = sqlite3.connect('promotions.db')
c = conn.cursor()



###########################################################################
### CREATE DATABASE TABLES ################################################
createTable_promotions = """
    CREATE TABLE IF NOT EXISTS 
        promotions( 
            transaction_id INT, 
            current_date TEXT,
            promotion_category TEXT,
            promotion_type TEXT,
            redemption_user TEXT,
            promotion_amount INT,
            notes TEXT
    )
"""
c.execute(createTable_promotions)