from PIL import Image

from newsletters_app.models import NewsletterUser
from shopping_app.models import Order


def resize_image(original_image):
    image = Image.open(original_image)
    img = image.resize((306, 259), Image.ANTIALIAS)
    return img


def get_context_attributes(request, user):
    if user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_quantity
        result = {
            'customer': customer,
            'order': order,
            'cart_items': cart_items,
            'items': items,
        }
        return result
    else:
        result = {
            'cart_items': 0,
        }
        return result


def get_user_subscription(user):
    if user.is_authenticated:
        subscribed_user = NewsletterUser.objects.filter(email=user.email)
        return subscribed_user
    else:
        subscribed_user = None
        return subscribed_user


