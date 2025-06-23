from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

#pagination class

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1

# Create your views here.
class ProductDRFview(APIView):
    def post(self, request):
        file =request.FILES.get('file')
        if not file.name.endswith('.xlsx'):
            return Response({"error": "File must be an Excel file (.xlsx)"}, status=status.HTTP_400_BAD_REQUEST)
        data = pd.read_excel(file)
        skipped = []
        for _, row in data.iterrows():
            product = {
                "Productname":row.get('Productname'),
                "description":row.get('description'),
                "price":row.get('price'),
                "stock":row.get('stock'),
                "HSN":row.get('HSN'),
                "mrp":row.get('mrp'),
                }
            if Product.objects.filter(HSN=product["HSN"]).exists():
                skipped.append({
                    "reason": "Duplicate HSN",
                    "data": product
                })
                continue
            serializer = ProductSerializer(data=product)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "message": "Upload complete",
            "skipped_rows": skipped
        }, status=status.HTTP_201_CREATED)
        
    def get(self, request):
        products = Product.objects.all()
        paginator = LargeResultsSetPagination()
        page = paginator.paginate_queryset(products, request)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    