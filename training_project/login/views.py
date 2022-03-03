import email
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from twilio.rest import Client
from .models import UserProfile

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)  
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class otp_verification(APIView):
    permission_classes = (IsAuthenticated,) 
    def post(self, request):
        data = request.data
        account_sid = 'ACb97a40ece94a39ad0b9897d8e9b2ca4f'
        auth_token = 'fa585b17ef8bbd74a31ef2ccc362f19b'
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                     body="Message from python",
                     from_='+19107271409',
                     to=data['phone_number']
                 )
        return Response(message.sid)

class User(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request):
        obj = UserProfile.objects.all()
        return Response(obj.values())
    def post(self, request):
        data = request.data
        obj = UserProfile(name = data["name"], email = data["email"], phone_number = data["phone_number"])
        obj.save()
        obj_id = obj.id
        return Response(obj_id)
    def update(self, request):
        id = request.GET
        data = request.data
        obj = UserProfile.objects.get(id = id)
        obj.name = data["name"]
        return Response(obj.id)

   