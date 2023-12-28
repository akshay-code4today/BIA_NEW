# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
import base64
import json

@api_view(['POST'])
def log_api(request):
    try:
        if request.method == 'POST':
            # Decode the base64-encoded email
            received_data = request.data
            encoded_email = received_data.get('email', '')
            decoded_email = base64.b64decode(encoded_email).decode("utf-8")
            "now we can use user master table to get the object related to this email and give this user access based on that"
            print("Decoded Email:", decoded_email)
            print("akshay3")

            return Response({"message": "Success"}, status=status.HTTP_200_OK)
    except json.JSONDecodeError as e:
        return Response({"error": f"JSON decode error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def get_all_books(request):
    try:
        if request.method == 'GET':
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"internal error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_book(request):
    try:
        if request.method == 'POST':
            print("akshay1")
            serializer = BookSerializer(data=request.data)
            print("akshay2")
            if serializer.is_valid():
                print("akshay3")
                serializer.save()
                print("aksjay4")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print("55555555555555555")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print("66666666666666666666666")
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"internal error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

