from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from shop.models import MyBag, Item, Customer
from .statuses import *


class MyBagView(View):

    def get(self, request):
        my_bags = MyBag.objects.all()
        data = []
        for my_bag in my_bags:
            data.append(
                {'id': my_bag.id, 'customer': str(my_bag.customer), 'items': str(my_bag.display_items()),
                 'total_price': str(my_bag.total_price)})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'customer_id' in data and 'item_ids' in data:
            try:
                items = Item.objects.filter(id__in=data['item_ids'])
                if len(data['item_ids']) == len(items):
                    my_bag = MyBag.objects.create(
                        customer=Customer.objects.get(pk=data['customer_id'])
                    )
                    for item in items:
                        my_bag.items.add(item)
                else:
                    return failed_status("No object with this id")
            except ObjectDoesNotExist:
                return failed_status("No object with this id")
        else:
            return failed_status("invalid_post_data")
        my_bag.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return MyBagView.get_by_id(request, id)
        if request.method == "PATCH":
            return MyBagView.edit(request, id)
        if request.method == "DELETE":
            return MyBagView.delete(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            my_bag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status({'id': my_bag.id, 'customer': str(my_bag.customer), 'items': str(my_bag.display_items()),
                            'total_price': str(my_bag.total_price)})

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            my_bag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if 'customer_id' in data:
            try:
                my_bag.customer = Customer.objects.get(pk=data['customer_id'])
            except ObjectDoesNotExist:
                return failed_status("No customer with this id")
        if 'item_ids' in data:
            try:
                items = Item.objects.filter(id__in=data['item_ids'])
                my_bag.items.clear()
                if len(data['item_ids']) == len(items):
                    for i in items:
                        my_bag.items.add(i)
                else:
                    return failed_status("No items with this id")
            except ObjectDoesNotExist:
                return failed_status("No items with this id")
        my_bag.save()
        return ok_status()

    @staticmethod
    def delete(request, id):
        try:
            my_bag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        my_bag.delete()
        return ok_status()
