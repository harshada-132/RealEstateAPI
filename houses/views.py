from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from .serializers import HouseSerializer
from rest_framework import generics
from .models import House

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    @action(detail=True, methods=['post'])
    def mark_sold(self, request, pk=None):
        try:
            house = self.get_object()
            house.sold = True
            house.save()
            return Response({'message': 'House marked as sold'}, status=status.HTTP_200_OK)
        except House.DoesNotExist:
            return Response({'error': 'House not found'}, status=status.HTTP_404_NOT_FOUND)
        
class HouseListAPIView(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    pagination_class = PageNumberPagination