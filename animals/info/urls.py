from django.urls import path
from . import views

urlpatterns = [
    path('family/<str:fam>', views.family),
    path('animal/<str:ani>', views.animal),
]