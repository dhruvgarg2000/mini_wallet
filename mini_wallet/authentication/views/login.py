from rest_framework.response import Response
from rest_framework import  status, viewsets
from rest_framework.decorators import action
from authentication.handlers.authentication import generate_jwt_token
from mini_wallet import settings
from wallet.models import User
from authentication.serializers.authentication import UserSerializer


class LoginViewSet(viewsets.ViewSet):

    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.create(**serializer.validated_data)
            return Response({"customer_id" : user.uuid}, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = User.objects.filter(username=username, password=password).first()
            if user:
                token = generate_jwt_token(str(user.uuid))
                return Response({
                                "token": token
                                })
            else:
                return Response("No matching users found.", status=status.HTTP_404_NOT_FOUND)