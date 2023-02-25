from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json
from django.contrib.auth.models import User

from shop.models import StoreOwner
from .statuses import *


class StoreOwnerView(View):

    def get(self, request):
        owners = StoreOwner.objects.all()
        data = []
        for owner in owners:
            data.append({'id': owner.id, 'user': str(owner.user), 'avatar': str(owner.avatar),
                         'registered_at': str(owner.registered_at)})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'user_id' in data:
            try:
                owner = StoreOwner.objects.create(
                    user=User.objects.get(pk=data['user_id']),
                )
            except ObjectDoesNotExist:
                return failed_status("No user with this id")
        else:
            return failed_status("invalid_post_data")
        if 'avatar' in data:
            owner.avatar = data['avatar']
        if 'registered_at' in data:
            owner.registered_at = data['registered_at']
        owner.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_by_id(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.edit(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.delete(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status({'id': owner.id, 'user': str(owner.user), 'avatar': str(owner.avatar),
                            'registered_at': str(owner.registered_at)})

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if 'user_id' in data:
            try:
                owner.user = User.objects.get(pk=data['user_id'])
            except ObjectDoesNotExist:
                return failed_status("No user with this id")
        if 'avatar' in data:
            owner.avatar = data['avatar']
        if 'registered_at' in data:
            owner.registered_at = data['registered_at']
        owner.save()
        return ok_status()

    @staticmethod
    def delete(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        owner.delete()
        return ok_status()
