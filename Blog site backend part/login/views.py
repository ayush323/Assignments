import email
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from twilio.rest import Client
from .models import UserProfile
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_500_INTERNAL_SERVER_ERROR
import random

class HelloView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content,status= HTTP_200_OK)

class otp_verification(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        data = request.data
        otp = random.randint(1000,9000)
        account_sid = 'ACb97a40ece94a39ad0b9897d8e9b2ca4f'
        auth_token = '61e6a12d18fe7f666e8e90580e82a4ac'
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                     body="your otp is {}".format(otp),
                     from_='+19107271409',
                     to='+918929185288'
                 )
        return Response(message.sid, status= HTTP_200_OK)

class User(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,) 
    def get(self, request):
        try:
          obj = request.user
          data = {}
          data["id"] = obj.id
          data["name"] = obj.username
          data["email"] = obj.email
          return Response(data, status= HTTP_200_OK)

        except Exception as err:
            import traceback
            traceback.print_exc()
            resp_json = {}
            resp_json["error"] = str(err)
            return Response(resp_json, status= HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        data = request.data
        obj = UserProfile(name = data["name"], email = data["email"], phone_number = data["phone_number"])
        obj.save()
        obj_id = obj.id
        return Response(obj_id, status= HTTP_200_OK)
    def update(self, request):
        id = request.GET
        data = request.data
        obj = UserProfile.objects.get(id = id)
        obj.name = data["name"]
        return Response(obj.id)

   