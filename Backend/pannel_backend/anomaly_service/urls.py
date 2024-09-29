from django.urls import path
from .views import AnomalyDetection_UnsuccessfullPayment, AnomalyDetection_SuccessfullPayment



urlpatterns = [
    path('unsuccessfull-payment-anomaly/', AnomalyDetection_UnsuccessfullPayment.as_view(), name='AnomalyDetection for UnsuccessfullPayment'),
    path('successfull-payment-anomaly/', AnomalyDetection_SuccessfullPayment.as_view(), name='AnomalyDetection for SuccessfullPayment-list'),

]