from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
#from player_app.authentication import ExpiringTokenAuthentication
from drfproj.settings import TOKEN_EXPIRE_TIME
from player_app.authentication import ExpiringTokenAuthentication
from player_app.models import Player
from player_app.serializers import PlayerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
import pytz
import datetime


class CustomAuthTokenLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        utc_now = datetime.datetime.now()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        result = Token.objects.filter(user=user, created__lt = utc_now - TOKEN_EXPIRE_TIME).delete()

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
# class CustomObtainToken(APIView):
#     permission_classes = []

#     def post(self, request, *args, **kwargs):
#         token = create_custom_token(request.user)
#         return Response({'token': token.key})

# class SomeSecuredView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         return Response({'message': 'You are authenticated!'})


@authentication_classes([ExpiringTokenAuthentication])
@permission_classes([IsAuthenticated])
class GetAllPlayersView(APIView):
    #permission_classes = (IsAuthenticated, )

    def get(self,request, *args, **kwargs):
        queryset = Player.objects.all().order_by('total_goals').values()
        serializer = PlayerSerializer(queryset,many=True)
        return Response(serializer.data)
    
class CreateNewPlayerView(APIView):
    #permission_classes = (IsAuthenticated, )

    def post(self,request,*args,**kwargs):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)