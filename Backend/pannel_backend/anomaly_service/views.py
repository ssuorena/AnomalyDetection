from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from .serializers import UnSuccessfulBuyPerDaysSerializer,SuccessfulBuyPerDaysSerializer
import pickle
import numpy as np

'''
Handles the POST request to calculate the anomaly factor based on unsuccessful buy per days data. 
If the serializer is valid, loads the model and predicts the anomaly factor using the input days data.
Returns the anomaly factor in the response if successful, otherwise returns serializer errors.
'''
class AnomalyDetection_UnsuccessfullPayment(APIView):
    @swagger_auto_schema(
        request_body=UnSuccessfulBuyPerDaysSerializer,
        responses={200: openapi.Response('Anomaly Detection for Daily Unsuccessfull Payment Signal with Isolated Forest Algorithm', UnSuccessfulBuyPerDaysSerializer)})
    def post(self, request, *args, **kwargs):
        """
        receive unsuccessfull payment in last for days and return an anomaly factor.
        input shape:
        {
            "days": [past1, past2, past3, past4]
        }
        -if anomlay factor == 1 : there is no anomaly
        -if anomlay factor == -1 : there is anomaly

        Example request:
        {
            "days": [5, 10, 5, 15]
        }

        Example response:
        {
            "Anomaly Factor": [1]
        }
        """

        serializer = UnSuccessfulBuyPerDaysSerializer(data=request.data)
        if serializer.is_valid():
            # load model:
            with open('anomaly_service/AI models/if_model_unsuccessfullPayment.pkl', 'rb') as f:
                clf_IF_us = pickle.load(f)
            
            days = serializer.validated_data['days']
            days = np.array(days)
            Anomaly_factor = clf_IF_us.predict(days.reshape(1,-1))
            return Response({'Anomaly Factor': Anomaly_factor}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    '''
Handles the POST request to calculate the anomaly factor based on successful buy per days data. 
If the serializer is valid, loads the model and predicts the anomaly factor using the input days data.
Returns the anomaly factor in the response if successful, otherwise returns serializer errors.
'''
class AnomalyDetection_SuccessfullPayment(APIView):
    @swagger_auto_schema(
        request_body=SuccessfulBuyPerDaysSerializer,
        responses={200: openapi.Response('Anomaly Detection for Daily Successfull Payment Signal with Isolated Forest Algorithm', SuccessfulBuyPerDaysSerializer)})
    def post(self, request, *args, **kwargs):
        """
        receive successfull payment in last for days and return an anomaly factor.
        input shape:
        {
            "days": [past1, past2, past3, past4]
        }
        -if anomlay factor == 1 : there is no anomaly
        -if anomlay factor == -1 : there is anomaly

        Example request:
        {
            "days": [5, 10, 5, 15]
        }

        Example response:
        {
            "Anomaly Factor": [1]
        }
        """
        serializer = SuccessfulBuyPerDaysSerializer(data=request.data)
        if serializer.is_valid():
            # load model:
            with open('anomaly_service/AI models/if_model_successfullPayment.pkl', 'rb') as f:
                clf_IF_us = pickle.load(f)
            
            days = serializer.validated_data['days']
            days = np.array(days)
            Anomaly_factor = clf_IF_us.predict(days.reshape(1,-1))
            return Response({'Anomaly Factor': Anomaly_factor}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)