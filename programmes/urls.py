from django.urls import path
from programmes.views import web, App, Machine, Data, Generic, Graphic, Software

app_name = 'programme'
urlpatterns = [
    path('web/', web, name='web'),
    path('app/', App.as_view(), name='app'),
    path('ma/', Machine.as_view(), name='ma'),
    path('data/', Data.as_view(), name='data'),
    path('gen/', Generic.as_view(), name='gen'),
    path('gra/', Graphic.as_view(), name='gra'),
    path('soft/', Software.as_view(), name='soft'),
]
