from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category


@api_view(['GET'])
def return_list(request):
    categories = [category.name for category in Category.objects.all()]
    return Response(categories)
