#pip install mysql-connector-python
#pip install tabulate
#pip install pandas openpyxl

import mysql.connector
import pandas as pd
from mysql.connector import Error
from tabulate import tabulate

#########INPUT#########
username = 'ellie'
password = 'E!!ie40028922'
host = 'localhost'
database = 'mydb'
output = 'PROMPT' # Choose how the output will be shown: EXCEL or PROMPT
#######################

if __name__ == '__main__':
    try:
        db_connection = mysql.connector.connect(host=host,
                                                   database=database,
                                                   user=username,
                                                   password=password)

        query_sent = """SELECT CONCAT(first_name, " ", last_name) AS "customer", COUNT(e.status) AS failures
                        FROM events e 
                        INNER JOIN campaigns camp 
                        ON e.campaign_id = camp.id
                        INNER JOIN customers cust
                        ON cust.id = camp.customers_id
                        WHERE e.status = "failure"
                        GROUP BY camp.customers_id
                        HAVING COUNT(e.status) > 3;"""

        cursor = db_connection.cursor()
        cursor.execute(query_sent)
        results = cursor.fetchall()

        headers = ["Customer", "Failures"]
        if output == 'PROMPT':
            table = tabulate(results, headers, tablefmt="pretty")
            print(table)
        elif output == 'EXCEL':
            df = pd.DataFrame(results, columns=headers)
            df.to_excel('customer_failures.xlsx', index=False)
            print("Results have been saved to customer_failures.xlsx")


    except Error as e:
        print("Error while executing query", e)
    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()
            #print("MySQL connection is closed")