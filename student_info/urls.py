from django.urls import path
from student_info.views import emma, christy, rob, imoh


app_name = 'student'
urlpatterns = [
    path('emma', emma, name='emma'),
    path('christy', christy, name='christy'),
    path('rob', rob, name='rob'),
    path('imoh', imoh, name='imoh'),
]