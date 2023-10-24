from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import numpy as np
import joblib

import pickle

# Load the saved model using pickle
with open('wine_quality_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

    
def predict_wine_quality(request):
    if request.method == 'POST':
        input_features = [
            float(request.POST['fixed_acidity']),
            float(request.POST['volatile_acidity']),
            float(request.POST['residual_sugar']),
            float(request.POST['total_sulfur_dioxide']),
            float(request.POST['density']),
            float(request.POST['pH']),
            float(request.POST['alcohol'])
        ]
        input_features_np = np.array(input_features).reshape(1, -1)
        prediction = model.predict(input_features_np)
        if prediction[0] == 1:
            result = 'Good Quality Wine'
        else:
            result = 'Bad Quality Wine'
        return render(request, 'result.html', {'result': result})
    return render(request, 'index.html')
