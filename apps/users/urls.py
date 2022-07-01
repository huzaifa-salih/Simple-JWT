from django.urls import path
from .views import UserAccountViews

urlspatterns = [
    path('', UserAccountViews.as_view()),

]