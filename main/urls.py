from django.urls import path
from main.views import contact, about, commentview, commentconfirm, Commview

app_name = 'met'
urlpatterns = [
    path('contact/', contact, name='con'),
    path('comment/', commentview, name='com'),
    path('about/', about, name='about'),
    path('com/', commentconfirm, name='conconfirm'),
    path('commview/', Commview.as_view(), name='commview'),


]