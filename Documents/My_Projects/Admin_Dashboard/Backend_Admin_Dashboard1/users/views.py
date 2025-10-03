from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterUserSerializer
from users.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated, AllowAny


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
