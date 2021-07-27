from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index),
    # path("february", views.index)
    path("", views.index),
    path("<int:month>", views.monthly_challenges_numbers),
    path("<str:month>", views.monthly_challenges,
         name="month-challenge")  # challenges/
]
