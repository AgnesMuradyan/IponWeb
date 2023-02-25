from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from shop.models import ItemCategory
from .statuses import *


class ItemCategoryView(View):

    def get(self, request):
        items = ItemCategory.objects.all()
        result = []
        for item in items:
            result.append({'id': item.id, 'name': item.name, 'picture': str(item.picture)})
        return data_status(result)

    def post(self, request):
        data = json.loads(request.body)
        if 'name' in data and 'picture' in data:
            item = ItemCategory.objects.create(
                name=data['name'],
                picture=data['picture'],
            )
        elif 'name' in data:
            item = ItemCategory.objects.create(
                name=data['name'],
            )
        elif 'picture' in data:
            item = ItemCategory.objects.create(
                picture=data['picture'],
            )
        else:
            return failed_status("invalid_post_data")
        item.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemCategoryView.get_by_id(request, id)
        if request.method == "PATCH":
            return ItemCategoryView.edit(request, id)
        if request.method == "DELETE":
            return ItemCategoryView.delete(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            item = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status({'id': item.id, 'name': item.name, 'picture': str(item.picture)})

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            item = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if 'name' in data:
            item.name = data['name']
        if 'picture' in data:
            item.picture = data['picture']
        item.save()
        return ok_status()

    @staticmethod
    def delete(request, id):
        try:
            item = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        item.delete()
        return ok_status()
