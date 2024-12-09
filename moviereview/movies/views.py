from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Movie Review API!"})
