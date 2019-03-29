from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """returns a list of APIView Features"""

        an_apiview = [
            'Uses HTTP methods sa functions',
            'this is similar to a traditional django view',
            'give control on logic'
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})
