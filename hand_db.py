from clickhouse_driver import Client
import pandas as pd

client = Client(
    host =  '172.17.0.2' ,
    user = 'default' ,
    password = '' , 
    port = 9000
)

#print(client.execute('SELECT version()')) 

client.execute('CREATE TABLE IF NOT EXISTS my_table (column1 Int32 , column2 String ) ENGINE = MergeTree() ORDER BY (column1)')

data = [
    (1 , 'String number one') , 
    (2 , 'String number two')
]


client.execute('INSERT INTO my_table (column1 , column2) VALUES' , data)

result = client.execute('SELECT * FROM my_table')
print(result)