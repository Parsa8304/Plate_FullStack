from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import PlateSerializer
from Plate_Api.models import Plate
from .image_proccessing import process_image



class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)


# class LoginView(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
        
#         user = authenticate(username=username, password=password)
#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key}, status=status.HTTP_200_OK)
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class PlateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PlateSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            plate_number = process_image(image)
            if plate_number is None:
                return Response({"error": "Failed to process image"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(
                image_name=image.name,
                plate_number=plate_number
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):    
        plates = Plate.objects.all()
        serializer = PlateSerializer(plates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)