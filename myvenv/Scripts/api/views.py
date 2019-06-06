from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . models import Talk
from . serializer import TalkSerializer
from rest_framework.decorators import api_view

from rest_framework.generics import GenericAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


class TalkView(ListModelMixin, CreateModelMixin, GenericAPIView):

    queryset = Talk.objects.all()
    serializer_class = TalkSerializer


    def perform_create(self, serializer):
        talk = get_object_or_404(Talk, talk_ID=self.request.data.get('talk_ID'))
        return serializer.save(talk=talk)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    '''
    def get(self, request):
        talks = Talk.objects.all()
        serializer = TalkSerializer(talks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TalkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        talks = get_object_or_404(Talk.objects.all(), pk=1)
        talks.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)

    def delete(self, request, pk):
        # Get object with this pk
        talk = get_object_or_404(Talk.objects.all(), pk=pk)
        talk.delete()
        return Response({"message": "Talk with id `{}` has been deleted.".format(pk)}, status=204)
    '''
class SingleTalkView(RetrieveAPIView):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer