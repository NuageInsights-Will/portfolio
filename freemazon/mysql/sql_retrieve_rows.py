import sqlite3
import pandas as pd

try: 
    connection = sqlite3.connect("online_store.db")
    query = "SELECT * FROM Customers;"
    result_df = pd.read_sql(query, connection)
    connection.close() #close the conection
    print(result_df.shape[0])

except Exception as e:
    connection.close()
    print(str(e))