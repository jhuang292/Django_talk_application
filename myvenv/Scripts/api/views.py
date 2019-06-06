from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . models import Talk
from . serializer import TalkSerializer

class TalkView(APIView):
    def get(self, request):
        talks = Talk.objects.all()
        serializer = TalkSerializer(talks, many=True)
        return Response(serializer.data)

    def post(self):
        pass



