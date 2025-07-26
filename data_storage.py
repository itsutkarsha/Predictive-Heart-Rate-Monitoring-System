# import csv
# import sqlite3

# # Function to store data in a CSV file
# def store_data_in_csv(data, prediction_result):
#     data_with_prediction = {**data, 'Prediction': prediction_result}

#     with open('predictions.csv', 'a', newline='') as csvfile:
#         fieldnames = list(data_with_prediction.keys())
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         # Write the header only once
#         if csvfile.tell() == 0:
#             writer.writeheader()

#         # Write the row with the input data and prediction
#         writer.writerow(data_with_prediction)

# # Function to store data in an SQLite database
# def store_data_in_db(data, prediction_result):
#     # Connect to SQLite database (it will be created if it doesn't exist)
#     conn = sqlite3.connect('predictions.db')
#     cursor = conn.cursor()

#     # Create the predictions table if it doesn't exist
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS predictions (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             age INTEGER,
#             sex INTEGER,
#             cholesterol INTEGER,
#             blood_pressure INTEGER,
#             prediction TEXT
#         )
#     ''')
#     conn.commit()

#     # Insert data into the database
#     cursor.execute('''
#         INSERT INTO predictions (age, sex, cholesterol, blood_pressure, prediction)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (data['age'], data['sex'], data['cholesterol'], data['blood_pressure'], prediction_result))
#     conn.commit()

#     # Close the database connection
#     conn.close()

# # Function to choose storage method (CSV or DB)
# def store_data(data, prediction_result, storage_method='csv'):
#     if storage_method == 'csv':
#         store_data_in_csv(data, prediction_result)
#     elif storage_method == 'db':
#         store_data_in_db(data, prediction_result)

import csv
import sqlite3

# Function to store data in a CSV file
def store_data_in_csv(data, prediction_result):
    # Include the 'name' field in the data along with the prediction
    data_with_prediction = {**data, 'Prediction': prediction_result}

    with open('predictions.csv', 'a', newline='') as csvfile:
        fieldnames = list(data_with_prediction.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only once
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write the row with the input data and prediction
        writer.writerow(data_with_prediction)

# Function to store data in an SQLite database
def store_data_in_db(data, prediction_result):
    # Connect to SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()

    # Create the predictions table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            sex INTEGER,
            cholesterol INTEGER,
            blood_pressure INTEGER,
            prediction TEXT
        )
    ''')
    conn.commit()

    # Insert data into the database
    cursor.execute('''
        INSERT INTO predictions (name, age, sex, cholesterol, blood_pressure, prediction)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (data['name'], data['age'], data['sex'], data['cholesterol'], data['blood_pressure'], prediction_result))
    conn.commit()

    # Close the database connection
    conn.close()

# Function to choose storage method (CSV or DB)
def store_data(data, prediction_result, storage_method='csv'):
    if storage_method == 'csv':
        store_data_in_csv(data, prediction_result)
    elif storage_method == 'db':
        store_data_in_db(data, prediction_result)
