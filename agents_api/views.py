from rest_framework import viewsets
from .models import Agent, Home, Buyer
from .serializers import AgentSerializer, HomeSerializer, BuyerSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def agent_view(request):
    agents = Agent.objects.all()
    serializer = AgentSerializer(agents, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def home_view(request):
    homes = Home.objects.all()
    serializer = HomeSerializer(homes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def buyer_view(request):
    buyers = Buyer.objects.all()
    serializer = BuyerSerializer(buyers, many=True)
    return Response(serializer.data)
