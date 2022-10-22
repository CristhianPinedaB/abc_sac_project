from django.db.models.signals import post_save,post_delete
#I have used django user model to use post save, post delete.
from applications.sales.models import Order,OrderItem
from django.dispatch import receiver
from decimal import Decimal
from django.db.models import Sum


# @receiver(post_delete, sender=OrderItem)
# def delete_order_item(sender, instance, **kwargs):
#     product = instance.product
#     product.quantity += instance.quantity
#     product.save()
    #instance.order.save()

# @receiver(post_save, sender=TransactionDetail, dispatch_uid="update_stock_count")
# def update_stock(sender, instance, **kwargs):
#     instance.product.stock -= instance.amount

#     post_save.disconnect(update_stock, sender=TransactionDetail)
#     instance.product.save()
#     post_save.connect(update_stock, sender=TransactionDetail)

@receiver(post_save,sender=Order)
def create_profile(sender,instance,created,**kwargs):
    if created:
        number_order = str(instance.created_at.year) + str(instance.number_id).zfill(5)
        instance.number_order = number_order
        # instance.save()
        #print('----------------signals---------------')
        # order_items = instance.items.all()
        # print('----------------signals---------------')
        # # print(order_items)

        # # instance.subtotal_amount = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
        # # instance.total_discount_amount = order_items.aggregate(Sum('discount_price'))['discount_price__sum'] if order_items.exists() else 0.00
        
        # instance.igv = round((int(18)/100)*float(instance.subtotal_amount), 2)
        # instance.total_amount = Decimal(instance.subtotal_amount) + Decimal(instance.igv)
        instance.save()
        
# @receiver(post_delete,sender=User)
# def delete_profile(sender,instance,*args,**kwargs):
#     #write your login when user profile is deleted.
#     print("User Profile Deleted").