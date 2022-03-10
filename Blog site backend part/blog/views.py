import imp

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_500_INTERNAL_SERVER_ERROR
from .models import post, Author, comments, Tag
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.views.generic import ListView , DetailView
from django.views import View
from django.http import HttpResponseRedirect

class Post(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        obj = post.objects.all()
        ans = []
        resp = {}
        for ob in obj:
            resp["title"] = ob.title
            resp["content"] = ob.content
            tags = []
            tmp = {}
            for tag in ob.tag.all():
                 tmp["caption"] = tag.caption
                 tmp["id"] = tag.id
                 tags.append(tmp)
                 tmp = {}
            resp["tags"] = tags     
            ans.append(resp)
            resp = {}      
        #resp = obj.values()
        
        return Response(ans, status = HTTP_200_OK)

    def post(self, request):
        data = request.data
        obj = post(title = data["title"], content = data["content"])
        author = Author.objects.get(id = data["author_id"])
        obj.author = author 
        obj.save()
        return Response(obj.id, status= HTTP_200_OK)

class PostDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = request.GET
        obj = post.objects.get(id = data["id"])
        
        if obj is None:
            raise Exception("No post found ")
        resp = {}
        resp["id"] = obj.id
        resp["title"] = obj.title
        resp["date"] = obj.data
        resp["content"] = obj.content
        resp["author"] = obj.author.FirstName
        return Response(resp, status = HTTP_200_OK)
     
    def update(self, request):
        data = request.data
        obj = post.objects.get(id = data["id"])
        if obj is None:
               raise Exception("no post found ")
        if data["title"]:
            obj.title = data["title"]

        if data["content"]:
            obj.content = data["content"]
        if data["author"]:
            author = Author.objects.get(id = data["author"])
            obj.author = author      
        return Response(obj.id, status= HTTP_200_OK)                 

class Authors(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        obj = Author.objects.all()
        if obj == None:
              raise Exception("No Author Found")
        else:      
          return Response(obj.values(), status= HTTP_200_OK)

    def post(self, request):
        data = request.data
        obj = Author(FirstName = data["FirstName"], LastName = data["LastName"], emailAddress = data["emailAddress"])
        obj.save()
        return Response(obj.id, status= HTTP_200_OK) 

class AuthorDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = request.GET
        try:
           obj = Author.objects.get(id = data["author_id"])
           resp = {}
           resp["FirstName"] = obj.FirstName
           resp["LastName"] = obj.LastName
           resp["emailAddress"] = obj.emailAddress
           return Response(resp, status = HTTP_200_OK)
        except:   
            raise Exception("No Author found")

class TagList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        obj = Tag.objects.all()
        final = []
        resp = {}
        tmpr = []
        for objec in obj:
          resp["caption"] = objec.caption
          tmp = {}
          for post in objec.post.all():
            tmp["title"] = post.title
            tmpr.append(tmp)
            tmp = {}
          resp["post"] = tmpr
          tmpr = []
          final.append(resp)
          resp = {}
        return Response(final, status= HTTP_200_OK)    
            
        


    






