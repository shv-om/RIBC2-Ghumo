from django.urls import path, include
from . import views

app = "market"

urlpatterns = [
        path('marketplace', views.marketplaceview.as_view(), name="marketplace"),
        path('event-details', views.eventdetailsview.as_view(), name="event-details"),
]