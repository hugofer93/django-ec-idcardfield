from django.forms import CharField

from ec_idcardfield.validators import (
    validate_idcard,
    validate_idcard_or_ruc,
    validate_ruc,
)


class IdcardField(CharField):
    default_validators = [validate_idcard, ]


class RUCField(CharField):
    default_validators = [validate_ruc, ]


class IdcardOrRUCField(CharField):
    default_validators = [validate_idcard_or_ruc, ]
