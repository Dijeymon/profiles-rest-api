from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API VIEW"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, delete)',
            'Is similar to a tradiotional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'messsage': 'Hello!', 'an_apiview': an_apiview})
