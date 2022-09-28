from django.shortcuts import render
import django.views.generic as views

from newsletters_app.models import NewsletterUser
from shopping_app.models import Order, Customer


class HomeView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            sub_user = NewsletterUser.objects.all().filter(email=self.request.user.email)
            customer, created = Customer.objects.get_or_create(user=user)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_quantity
            if sub_user:
                context = {
                    'subscribed_user': sub_user,
                    'cart_items': cart_items,
                    'user': user,
                }
                return context
            else:
                context = {
                    'cart_items': cart_items,
                    'user': user,
                }
                return context
        else:
            order = {'get_cart_total': 0, 'get_cart_quantity': 0, }
            cart_items = order['get_cart_quantity']

            context = {
                'user': user,
                'order': order,
                'cart_items': cart_items,
            }
            return context


def show_gallery(request):
    return render(request, 'gallery-1.html')
