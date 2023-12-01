# from settings import *
from django.core.mail import send_mail
from django.conf import settings

settings.configure(
    # EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',
    EMAIL_HOST='smtp.163.com',
    EMAIL_PORT=25,
    EMAIL_HOST_USER='heyanah@163.com',
    EMAIL_HOST_PASSWORD='OUNLZEPFWZXFPYKS',
    EMAIL_USE_SSL=False,
)

send_mail('Django mail', 'This e-mail was sent with Django.',
          'heyanah@163.com', ['1460185042@qq.com'])
