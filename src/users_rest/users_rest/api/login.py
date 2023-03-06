from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
import json
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed


@api_view(['POST'])
@permission_classes((~IsAuthenticated,))
def login(request):
    data = json.loads(request.body.decode("utf-8"))
    try:
        username = data['username']
        password = data['password']
    except KeyError:
        return Response("Key_error")
    user = authenticate(username=username, password=password)
    if user is not None:
        # if not user.is_active:
        #     return Response({'error': 'User is not active'})
        token = RefreshToken.for_user(user)
        return Response({'status': 'logged in', 'access': str(token.access_token), 'refresh': str(token)})
    return Response({'error': 'Invalid credentials'})
    # raise AuthenticationFailed("user_not_found")
