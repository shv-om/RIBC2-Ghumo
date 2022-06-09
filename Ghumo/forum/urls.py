from django.urls import path, include
from . import views

app = 'forum'

urlpatterns = [
        path('faq', views.faqview.as_view(), name="faq"),
]
