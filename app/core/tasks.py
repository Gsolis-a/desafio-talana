from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email():
    send_mail('celery works',
              'link para confirmar tu correo aqui',
              'correo@inserteaqui.cl',
              ['correo@inserteaqui.cl'])
    return None
