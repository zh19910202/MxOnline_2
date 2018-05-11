# _*_ coding: utf-8 _*_
__author__ = 'HeYang'

from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline_2.settings import EMAIL_FORM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()

    # ORM存储邮箱验证
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    # 发送邮件方法
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "何阳在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/%s" %(code)

        # 发送成功为True，失败为False
        send_status = send_mail(email_title, email_body, EMAIL_FORM, [email])

        return send_status
    elif send_type == "forget":
        email_title = "何阳在线网密码重置链接"
        email_body = "请点击下面的链接重置你的密码: http://127.0.0.1:8000/reset/%s" % (code)

        # 发送成功为True，失败为False
        send_status = send_mail(email_title, email_body, EMAIL_FORM, [email])

        return send_status


