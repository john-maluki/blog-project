from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_contact_email(email, message):
    c = {'email': email, 'message': message}

    email_subject = render_to_string(
        'contact/email/contact_email_subject.txt', c).replace('\n', '')
    email_body = render_to_string('contact/email/contact_email_body.txt', c)

    email = EmailMessage(
        email_subject, email_body, email,
        [settings.DEFAULT_FROM_EMAIL], [],
        headers={'Reply-To': email}
    )
    return email.send(fail_silently=False)


def send_periodic_email():
    # send_mail(subject, message, from_email,
    # recipient_list, fail_silently=False,
    # auth_user=None, auth_password=None,
    # connection=None, html_message=None)
    send_mail(
        'Did you get this subject',  # subject
        'message: did you?.',        # message
        'john.maluki@gmail.com',          # sender
        ['joe@mumyi.online'],          # recipient
        fail_silently=False,         # raise exception if error
    )
