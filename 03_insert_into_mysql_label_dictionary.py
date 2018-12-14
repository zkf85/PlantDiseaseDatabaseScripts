# KF 12/12/2018

# Insert labelNumber_to_plant_disease data into database
# Reference:
#   https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

import mysql.connector
import numpy as np

# 1. import data:
data = np.load('labelNum_to_labelName.npy')
data = data.tolist()

database_name = 'PlantDiseaseLibrary'
table_name = 'model_label_dictionary'

# 2. Create mysql connector and cursor
#conn = mysql.connector.connect(user='kefeng', password='qqq', database=database_name)
conn = mysql.connector.connect(host='192.168.1.235', user='kefeng', password='qqq', database=database_name)
cursor=conn.cursor()

# mysql insert statements:
add_piece = ("INSERT INTO model_label_dictionary "
               "(label_id, article_id, plant_name, health_status, disease_name, severity) " 
               "VALUES (%(label_id)s, %(article_id)s, %(plant_name)s, %(health_status)s, %(disease_name)s, %(severity)s)")

# 3. Insertion
for key in data.keys():
    
    # Determine health status and disease name
    health_status = 0
    disease_name = None
    severity = None
    if data[key][1] != 'healthy':
        health_status = 1
        disease_name = data[key][1]
        # Determine severity:
        if len(data[key]) == 3:
            if data[key][-1] == 'general':
                severity = 0
            elif data[key][-1] == 'serious':
                severity = 1

    piece = {
        'label_id': key,
        'article_id': None,
        'plant_name': data[key][0],
        'health_status': health_status,
        'disease_name': disease_name,
        'severity': severity,
    }
    cursor.execute(add_piece, piece)

conn.commit()

cursor.close()
conn.close()
