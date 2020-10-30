from django.urls import path
from .views import complainttview, Complaint2, pay, enrolview, Enroll, confirm, enroldetailview, Enrolldetail, Enrolprint


app_name = 'quick'

urlpatterns = [
    path('complaint2/', Complaint2.as_view(), name='complaint2'),
    path('complaint/', complainttview, name='complaint'),
    path('payment/', pay, name='pay'),
    path('enrol/', enrolview, name='enrol'),
    path('confirm/', confirm, name='confirm'),
    path('end/', Enroll.as_view(), name='en'),
    path('end/', Enroll.as_view(), name='end'),
    path('<int:pk>/', Enrolldetail.as_view(), name='enddetail'),
    path('<detail/', enroldetailview, name='detail'),

    path('formprint/', Enrolprint.as_view(), name='print'),
]