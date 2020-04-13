from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from user.models import USERNAME_MAX_LENGTH, USERNAME_MIN_LENGTH


def validate_username(username):
    if len(username) < USERNAME_MIN_LENGTH:
        raise ValidationError(
            _('username %(value) does not respect minimum length (%d chars)' % USERNAME_MIN_LENGTH),
            params={'value': username},
        )

    if len(username) > USERNAME_MAX_LENGTH:
        raise ValidationError(
            _('username %(value) does not respect maximum length (%d chars)' % USERNAME_MAX_LENGTH),
            params={'value': username},
        )

