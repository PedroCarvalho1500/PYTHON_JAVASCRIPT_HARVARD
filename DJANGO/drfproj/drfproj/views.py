from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from player_app.models import Player
from player_app.serializers import PlayerSerializer


class GetAllPlayersView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self,request, *args, **kwargs):
        queryset = Player.objects.all().order_by('total_goals').values()
        serializer = PlayerSerializer(queryset,many=True)
        return Response(serializer.data)
    
class CreateNewPlayerView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self,request,*args,**kwargs):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)