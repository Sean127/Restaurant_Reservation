from . import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='home'),
    path('reservation', views.ReservationView.as_view(), name='reservation')

]