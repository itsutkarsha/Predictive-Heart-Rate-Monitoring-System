
# from flask import Flask, request, jsonify, render_template
# import pickle
# import pandas as pd

# # Initialize Flask app
# app = Flask(__name__)

# # Load the trained model and columns used for training
# model = pickle.load(open('heart_disease_rf_model.pkl', 'rb'))
# columns = pickle.load(open('X_train_columns.pkl', 'rb'))
# @app.route('/')
# def home():
#     return render_template('home.html')

# # Route for the prediction page
# @app.route('/predict_page')
# def predict_page():
#     return render_template('index.html')

# # Prediction route for making predictions
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get data from form input
#     data = request.form.to_dict()

#     # Convert input data to DataFrame with same columns as training data
#     patient_df = pd.DataFrame([data])
#     patient_df = pd.get_dummies(patient_df)
    
#     # Add any missing columns and order columns to match training data
#     for col in columns:
#         if col not in patient_df:
#             patient_df[col] = 0
#     patient_df = patient_df[columns]

#     # Make prediction
#     prediction = model.predict(patient_df)[0]
#     result = "The patient is predicted to have heart disease." if prediction == 1 else "The patient is predicted NOT to have heart disease."

#     # Return the result
#     return render_template('index.html', prediction_text=result)

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify, render_template
# import pickle
# import pandas as pd
# from data_storage import store_data  # Import the function from the new file

# # Initialize Flask app
# app = Flask(__name__)

# # Load the trained model and columns used for training
# model = pickle.load(open('heart_disease_rf_model.pkl', 'rb'))
# columns = pickle.load(open('X_train_columns.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('home.html')

# # Route for the prediction page
# @app.route('/predict_page')
# def predict_page():
#     return render_template('index.html')

# # Prediction route for making predictions
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get data from form input
#     data = request.form.to_dict()

#     # Convert input data to DataFrame with same columns as training data
#     patient_df = pd.DataFrame([data])
#     patient_df = pd.get_dummies(patient_df)
    
#     # Add any missing columns and order columns to match training data
#     for col in columns:
#         if col not in patient_df:
#             patient_df[col] = 0
#     patient_df = patient_df[columns]

#     # Make prediction
#     prediction = model.predict(patient_df)[0]
#     result = "The patient is predicted to have heart disease." if prediction == 1 else "The patient is predicted NOT to have heart disease."

#     # Store the data and prediction (choose 'csv' or 'db' for storage method)
#     storage_method = 'csv'  # Or 'db' for database storage
#     store_data(data, result, storage_method)

#     # Return the result
#     return render_template('index.html', prediction_text=result)

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, render_template
import pickle
import pandas as pd
from data_storage import store_data  # Import the function from the new file

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and columns used for training
model = pickle.load(open('heart_disease_rf_model.pkl', 'rb'))
columns = pickle.load(open('X_train_columns.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

# Route for the prediction page
@app.route('/predict_page')
def predict_page():
    return render_template('index.html')

# Prediction route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form input
    data = request.form.to_dict()

    # Convert input data to DataFrame with same columns as training data
    patient_df = pd.DataFrame([data])
    patient_df = pd.get_dummies(patient_df)
    
    # Add any missing columns and order columns to match training data
    for col in columns:
        if col not in patient_df:
            patient_df[col] = 0
    patient_df = patient_df[columns]

    # Make prediction
    prediction = model.predict(patient_df)[0]
    result = "The patient is predicted to have heart disease." if prediction == 1 else "The patient is predicted NOT to have heart disease."

    # Store the data and prediction (choose 'csv' or 'db' for storage method)
    storage_method = 'csv'  # Or 'db' for database storage
    store_data(data, result, storage_method)

    # Return the result
    return render_template('index.html', prediction_text=result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
