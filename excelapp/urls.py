from django.urls import path

from . import views
urlpatterns = [
    path('doc/',views.AnalyseFile.as_view(),name="file analyser"),
]
