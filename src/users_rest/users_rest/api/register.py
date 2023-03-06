from __future__ import absolute_import
import json
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from rest_framework.permissions import AllowAny
from auth_app.models import VerificationCode


@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    data = json.loads(request.body)
    try:
        username = data['username']
        email = data['email']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
    except KeyError:
        return HttpResponse("key_error")
    if User.objects.filter(email=email).exists():
        return Response({'error': "email_is_already_registered"})
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.is_active = False
    user.save()
    us_ver = VerificationCode(user=user)
    us_ver.save()
    send_conf_email(us_ver)
    return Response({"status": "registered"})


def send_conf_email(us_ver):
    send_mail(
        subject='Verification Email',
        message=strip_tags(render_to_string("mail.html", {"username": us_ver.user.username,
                                                          "verification_code": us_ver.verification})),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[us_ver.user.email])

    return Response({"status": "email_sent"})

