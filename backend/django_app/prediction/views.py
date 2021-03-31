from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
import numpy as np
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from prediction.apps import DiabapiConfig
# Create your views here.
# Class based view to predict based on diabetes model
class Deabetes_Model_Predict(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data_dict = request.data

        keys=[]
        values=[]
        for key in data_dict:
            keys.append(key)
            values.append(data_dict[key])
        
        values_nparray = np.array(values)
        # print(values_nparray)
 
        scaler = DiabapiConfig.scaler
        # print(scaler)
        scaled_data = scaler.transform(values_nparray.reshape(1,-1))
        # print(scaled_data)

        prediction = DiabapiConfig.classifier.predict(scaled_data)

        y_pred = pd.Series(prediction)
        target_map = {0: 'No Diabetes', 1: 'Diabetes Detected'}
        y_pred = y_pred.map(target_map).to_numpy()
        response_dict = {"Prediced Diabetes status": y_pred[0]}

        return Response(response_dict, status=200)




        # print(prediction)
        # if prediction == 1:
        #     result = "Diabetes Detected"
        # else:
        #      result = "No Diabetics"

        # # Add data to db
        # obj = Diabetes()
        # obj.Pregnancies = values[0]
        # obj.Glucose = values[1]
        # obj.BloodPressure = values[2]
        # obj.SkinThickness = values[3]
        # obj.Insulin = values[4]
        # obj.BMI = values[5]
        # obj.DiabetesPedigreeFunction = values[6]
        # obj.Age = values[7]
        # obj.Prediction = result
        # obj.save()

        # obj2 = Teacher()
        # obj2.name = "Faysal"
        # obj2.gender = "male"
        # obj2.age = 23
        
        # obj2.save()

        
        # return Response(result,status=200)