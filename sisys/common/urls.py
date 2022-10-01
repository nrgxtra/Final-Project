from django.urls import path

from common.views import show_about, ServicesView, ServiceDetailView, list_services_by_category, make_appointment

urlpatterns = [
    path('about/', show_about, name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('service-details/<int:pk>', ServiceDetailView.as_view(), name='service_details'),
    path('service-category/<cat>', list_services_by_category, name='service_category'),
    path('appointment/', make_appointment, name='make_appointment'),

]
