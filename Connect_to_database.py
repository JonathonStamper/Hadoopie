import pandas as pd
import pyodbc

# Set up database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-QOE424AL\SQLEXPRESS01;'
                      'Database=Week9;'
                      'Trusted_Connection=yes;')

# Read CSV files
df1 = pd.read_csv('sentiment_categories.csv')
df2 = pd.read_csv('Image_colors.csv')

# Insert data into SQL Server table
cursor = conn.cursor()

create_review_table = 'CREATE TABLE Review (review TEXT, sentiment TEXT)'
cursor.execute(create_review_table)

create_image_table = 'CREATE TABLE Images (image TEXT, color TEXT)'
cursor.execute(create_image_table)

# Insert data from file1.csv
for index, row in df1.iterrows():
    cursor.execute("INSERT INTO Review (review, sentiment) VALUES (?, ?)", row['H&M_Review'], row['Sentiment Category'])

# Insert data from file2.csv
for index, row in df2.iterrows():
    cursor.execute("INSERT INTO Images (image, color) VALUES (?, ?)", row['image_url'], row['color'])

conn.commit()
conn.close()