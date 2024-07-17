from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
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

    @action(detail=False, methods=['get'])
    def by_phone(self, request):
        phone = request.query_params.get('phone', None)
        if phone is not None:
            buyers = Buyer.objects.filter(phone=phone)
            serializer = self.get_serializer(buyers, many=True)
            return Response(serializer.data)
        return Response({"detail": "Phone number not provided"}, status=400)

    @action(detail=False, methods=['get'])
    def search(self, request):
        phone = request.query_params.get('phone')
        email = request.query_params.get('email')
        if phone and email:
            buyers = Buyer.objects.filter(phone=phone, email=email)
            serializer = self.get_serializer(buyers, many=True)
            return Response(serializer.data)
        return Response({"detail": "Phone number and email required"}, status=400)

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
