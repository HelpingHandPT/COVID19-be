from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import MyUserSerializer
from user.models import MyUser

class MyUserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
