from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

from .serializers import UserSerializer
from .utils import decode_uid, encode_uid


def email_activation(user):
    template = "activation_email.html"

    token = default_token_generator.make_token(user)
    uid = encode_uid(user.username)

    body = get_template(template).render(
        {"username": user.username, "url": f"activate/{uid}/{token}/"}
    )

    mail = EmailMessage(
        subject="rekindled.io - User Activation",
        body=body,
        from_email=settings.EMAIL["FROM"],
        to=[user.email],
        reply_to=settings.EMAIL["REPLY_TO"],
    )
    mail.content_subtype = "html"

    return mail
