from rest_framework import generics
from .models import CallRecord
from .serializers import CallRecordSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateAPIView(generics.CreateAPIView):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer

class RetrieveAPIView(generics.RetrieveAPIView):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer

class AggregationAPIView(APIView):
    def get(self, request):
        data = CallRecord.objects.values('caller_name').annotate(total_calls=Count('caller_name')).order_by('-total_calls')
        return Response(data)
