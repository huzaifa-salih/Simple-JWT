from django.contrib.auth import get_user_model as User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class UserAccountViews(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            username = data["username"]
            email = data["email"]
            email = email.lower()
            password = data["password"]
            re_password = data["re_password"]
            is_superuser = data["is_superuser"]

            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():
                        if not is_superuser:
                            User.objects.create_user(username=username, email=email, password=password)
                            return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
                        else:
                            User.objects.create_superuser(username=username, email=email, password=password)
                            return Response({"success": "Superuser account created successfully"}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"error": "User with this account already exists."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"error": "Password must be at least 8 characters in length"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "Something went wrong when registering an account"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
