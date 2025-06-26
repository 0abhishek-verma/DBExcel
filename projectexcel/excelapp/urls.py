from django.urls import path
from .views import *

urlpatterns = [
    path('excel/', ProductDRFview.as_view(), name='ProductDRFview'),
    path('excel-download/', DownloadExcel.as_view(), name='DownloadExcel'),
]
