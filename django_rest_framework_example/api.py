# from rest_framework import status
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from catalogos.models import (Pais)
# from catalogos.serializers import (PaisSerializer)
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
#
#
# class PaisesAPI(APIView):
#     permission_classes =
#
#
#     def get(self, request):
#         paises = Pais.objects.all()
#         serializer = PaisSerializer(paises, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         paises = Pais.objects.all()
#         serializer = PaisSerializer(paises, many=True)
#         return Response(serializer.data)
#
#
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
# from rest_framework_simplejwt.views import TokenViewBase
#
#
# class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):
#
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
#         data['id'] = self.user.id
#         data['username'] = self.user.username
#         return data
#
#
# class TokenObtainPairView(TokenViewBase):
#     """
#         Return JWT tokens (access and refresh) for specific user based on username and password.
#     """
#     serializer_class = TokenObtainLifetimeSerializer
#
#
# class LogoutAPI(APIView):
#     """Blacklist the refresh token: extract token from the header
#       during logout request user and refresh token is provided"""
#
#     def post(self, request):
#         token = RefreshToken(request.data.get('refresh'))
#         token.blacklist()
#
#         return Response("Successful Logout", status=status.HTTP_200_OK)
