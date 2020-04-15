from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from user.models import USERNAME_MAX_LENGTH, USERNAME_MIN_LENGTH


def validate_username(username):
    if len(username) < 5:
        raise ValidationError(
            _('username %(value) does not respect minimum length (%d chars)' % 5),
            params={'value': username},
        )

    if len(username) > 20:
        raise ValidationError(
            _('username %(value) does not respect maximum length (%d chars)' % 20),
            params={'value': username},
        )

