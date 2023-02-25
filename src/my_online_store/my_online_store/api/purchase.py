from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
# import json

from shop.models import Purchase, Item, Customer
from .statuses import *
from copy import deepcopy, copy


class PurchaseView(View):

    def get(self, request):
        purchases = Purchase.objects.all()
        data = []
        for purchase in purchases:
            data.append({'id': purchase.id, 'items': str(purchase.display_items()), 'buy_time': str(purchase.buy_time),
                         'customer': str(purchase.customer), 'total_price': str(purchase.total_price)})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'item_ids' in data and 'customer_id' in data:
            try:
                items = Item.objects.filter(id__in=data['item_ids'])
                if len(data['item_ids']) == len(items):
                    purchase = Purchase.objects.create(
                        customer=Customer.objects.get(pk=data['customer_id'])
                    )
                    for item in items:
                        if item.quantity > 0:
                            purchase.items.add(item)
                            item.quantity -= 1
                            item.save()
                        else:
                            purchase.delete()
                            return failed_status("There is no item you want to add")
                else:
                    return failed_status("No item with this id")
            except ObjectDoesNotExist:
                return failed_status("No object with this id")
        else:
            return failed_status("invalid_post_data")
        purchase.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return PurchaseView.get_by_id(request, id)
        if request.method == "PATCH":
            return PurchaseView.edit(request, id)
        if request.method == "DELETE":
            return PurchaseView.delete(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status(
            {'id': purchase.id, 'items': str(purchase.display_items()), 'buy_time': str(purchase.buy_time),
             'customer': str(purchase.customer), 'total_price': str(purchase.total_price)})

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if 'customer_id' in data:
            try:
                purchase.customer = Customer.objects.get(pk=data['customer_id'])
            except ObjectDoesNotExist:
                return failed_status("No customer with this id")
        if 'item_ids' in data:
            try:
                items = Item.objects.filter(id__in=data['item_ids'])
                curr = copy(purchase.items.all())
                purchase.items.clear()
                if len(data['item_ids']) == len(items):
                    for item in items:
                        if item.quantity > 0:
                            purchase.items.add(item)
                            item.quantity -= 1
                            item.save()
                        else:
                            # purchase.delete()
                            purchase.items.set(curr)
                            return failed_status("There is no item you want to add")
                else:
                    return failed_status("No items with this id")
            except ObjectDoesNotExist:
                return failed_status("No items with this id")
        if 'buy_time' in data:
            purchase.buy_time = data['buy_time']
        purchase.save()
        return ok_status()

    @staticmethod
    def delete(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        purchase.delete()
        return ok_status()
