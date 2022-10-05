from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer , LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import login , logout 
# Create your views here.

class SignUpView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save() # call serializer.create()
            response = {
                "message": "User Created Successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):

    serializer_class = LoginSerializer
    permission_classes = []

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            response = {"message": "Login Successfull" ,"token": user.auth_token.key}
            return Response(data=response, status=status.HTTP_200_OK)
    
    def get(self, request:Request):
        user = request.user
        if user.is_authenticated:
            response = {"message": "You are Logged in.", "user": user.username}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            response = {"message": "You are not logged in"}
            return Response(data=response, status=status.HTTP_401_UNAUTHORIZED)
        
            

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        response = {"message": "Logout Successfull"}
        return Response(data=response, status=status.HTTP_202_ACCEPTED)



     