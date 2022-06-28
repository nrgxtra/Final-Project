from sisys.celery import app


@app.task(name='send_subscription_mail')
def send_subscription_mail(request):
    pass

