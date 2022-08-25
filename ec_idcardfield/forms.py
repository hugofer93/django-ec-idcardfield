from django.forms import CharField

from ec_idcardfield.validators import (
    validate_idcard,
    validate_idcard_or_ruc,
    validate_ruc,
)


class IdcardField(CharField):
    default_validators = [validate_idcard, ]

    def __init__(self, **kwargs):
        kwargs.setdefault('max_length', validate_idcard.NUMBER_DIGITS)
        kwargs.setdefault('min_length', validate_idcard.NUMBER_DIGITS)
        super().__init__(**kwargs)


class RUCField(CharField):
    default_validators = [validate_ruc, ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', validate_ruc.NUMBER_DIGITS)
        kwargs.setdefault('min_length', validate_ruc.NUMBER_DIGITS)
        super().__init__(**kwargs)


class IdcardOrRUCField(CharField):
    default_validators = [validate_idcard_or_ruc, ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', validate_ruc.NUMBER_DIGITS)
        kwargs.setdefault('min_length', validate_idcard.NUMBER_DIGITS)
        super().__init__(**kwargs)
