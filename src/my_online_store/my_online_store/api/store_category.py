from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from shop.models import StoreCategory
from .statuses import *


class StoreCategoryView(View):

    def get(self, request):
        stores = StoreCategory.objects.all()
        result = []
        for store in stores:
            result.append({'id': store.id, 'name': store.name, 'picture': str(store.picture)})
        return data_status(result)

    def post(self, request):
        data = json.loads(request.body)
        if 'name' in data and 'picture' in data:
            category = StoreCategory.objects.create(
                name=data['name'],
                picture=data['picture'],
            )
        elif 'name' in data:
            category = StoreCategory.objects.create(
                name=data['name'],
            )
        elif 'picture' in data:
            category = StoreCategory.objects.create(
                picture=data['picture'],
            )
        else:
            return failed_status('invalid_post_data')
        category.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategoryView.get_by_id(request, id)
        if request.method == "PATCH":
            return StoreCategoryView.edit(request, id)
        if request.method == "DELETE":
            return StoreCategoryView.delete(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status({'id': category.id, 'name': category.name, 'picture': str(category.picture)})

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if 'name' in data:
            category.name = data['name']
        if 'picture' in data:
            category.picture = data['picture']
        category.save()
        return ok_status()

    @staticmethod
    def delete(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        category.delete()
        return ok_status()


