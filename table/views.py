from django.shortcuts import render

from .models import Pack
from .serializers import PackSerializer
# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response




# class PackList(generics.ListAPIView):
#     queryset = Pack.objects.all()
#     serializer_class = PackSerializer

class PackList(APIView):
  def get(self,request):
    packs = Pack.objects.all()
    serialized = PackSerializer(packs, many=True)
    return Response(serialized.data)
  
    # def get_queryset(self):
    #     return super().get_queryset()

# class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializer

def packs(request):
  return render (request, 'index.html')
