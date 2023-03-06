from django.contrib import admin
from django.urls import path, include
from .api.register import register
from .api.verification import verification
from .api.login import login
from .api.logout import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('verify/', verification),
    path('login/', login),
    path('logout/', logout)
]
