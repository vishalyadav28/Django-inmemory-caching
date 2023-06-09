from django.core.cache import cache
from users.models import User
from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from datetime import timedelta
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser

class AverageAPIViewset(viewsets.ViewSet):
    parser_classes         = (MultiPartParser,)

    # Create Project Api
    @action(methods=['GET' ], detail=False)
    def average_age(self,request):
        # Try to get the average age from cache
        average_age = cache.get('average_age')

        if not average_age:
            # Calculate the average age if it's not in the cache
            average_age = User.objects.aggregate(Avg('age'))['age__avg']

            # Store the average age in cache for 5 seconds
            cache.set('average_age', average_age, 5)

        return Response({'average_age': average_age})