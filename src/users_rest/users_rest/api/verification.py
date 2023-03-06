from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from auth_app.models import VerificationCode
import json
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes((AllowAny,))
def verification(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        email = data['email']
        verification_code = data['verification_code']
    except KeyError:
        return Response("key_error")
    try:
        us_ver = VerificationCode.objects.get(user__email=email)
        if us_ver.verification_code == verification_code:
            us_ver.user.is_active = True
            us_ver.user.save()
            return Response("verified_successfully")
    except ObjectDoesNotExist:
        return Response("no_such_email")
    return Response("verification_code_is_wrong")
