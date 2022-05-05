import pandas as pd
import sqlite3

connection = sqlite3.connect("online_store.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS Zillow")
cursor.execute("DROP TABLE IF EXISTS zillow_cleaned")
cursor.execute("CREATE TABLE zillow_cleaned (IndexNum INTEGER PRIMARY KEY, LivingSpace_sq_ft INTEGER, Beds INTEGER, Baths FLOAT, YearBuilt INTEGER, ListPrice_dollars INTEGER, LivingSpaceGreaterThan2000 BOOLEAN, TotalRooms FLOAT, ListPriceInclTax FLOAT, EstMortgageFees FLOAT);")

data = pd.read_csv('zillow_cleaned.csv', index_col = 0)
data.columns = ["LivingSpace_sq_ft", "Beds", "Baths", "YearBuilt", "ListPrice_dollars", "LivingSpaceGreaterThan2000", "TotalRooms", "ListPriceInclTax", "EstMortgageFees"]
data.to_sql('zillow_cleaned', connection, if_exists='append', index=False)

connection.commit()
connection.close()