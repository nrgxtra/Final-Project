from django.urls import path

from common.views import show_about, ServicesView, ServiceDetailView, list_services_by_category, make_appointment, \
    BookingSuccess, GalleryView, FaqView, TermsView, PrivacyView, send_question, QuestionSentView

urlpatterns = [
    path('about/', show_about, name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('service-details/<int:pk>', ServiceDetailView.as_view(), name='service_details'),
    path('service-category/<cat>', list_services_by_category, name='service_category'),
    path('appointment/', make_appointment, name='make_appointment'),
    path('booking-success/', BookingSuccess.as_view(), name='booking_success'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('contact/', send_question, name='contact'),
    path('question-sent/', QuestionSentView.as_view(), name='question_sent'),
]
