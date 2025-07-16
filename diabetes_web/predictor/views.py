from django.shortcuts import render
import numpy as np
import joblib
import os

# Load model and scaler from app directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, 'diabetes_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))

def index(request):
    return render(request, 'predictor/index.html')

def predict(request):
    if request.method == 'POST':
        try:
            # Field order must match model training
            fields = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                      'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
            
            # Get values from form input
            input_values = [float(request.POST.get(field)) for field in fields]

            # Scale and predict
            scaled_input = scaler.transform([input_values])
            prediction = model.predict(scaled_input)[0]

            result = 'Diabetic' if prediction == 1 else 'Not Diabetic'

        except Exception as e:
            result = f"Error: {str(e)}"

        # Show result only after POST
        return render(request, 'predictor/index.html', {'result': result})
    
    # Don't show result on first visit / refresh
    return render(request, 'predictor/index.html')
