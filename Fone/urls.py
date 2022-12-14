from django.urls import path
from .views import FoneListView, FoneDetailView, CircuitsListView, CircuitsDetailView

urlpatterns = [
    path("Fone/", FoneListView.as_view(), name="Fone_list"),
    path("Fone/<int:pk>", FoneDetailView.as_view(), name="Fone_detail"),
    path("circuits/", CircuitsListView.as_view(), name="circuits_list"),
    path("circuits/<int:pk>", CircuitsDetailView.as_view(), name="circuits_detail"),
]
