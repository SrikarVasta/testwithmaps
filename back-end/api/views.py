from rest_framework.response import Response
from rest_framework.decorators import api_view
from geodata.models import Shape
from .serializers import ShapeSerializer
from api import serializers


@api_view(['GET'])
def getData(request):
    shapes = Shape.objects.all()
    serializer = ShapeSerializer(shapes, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def addShape(request):
    serializer = ShapeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
