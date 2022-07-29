from django.db.models import CharField

from ec_idcardfield.forms import (
    IdcardField as FormIdcardField,
    IdcardOrRUCField as FormIdcardOrRUCField,
    RUCField as FormRUCField,
)
from ec_idcardfield.validators import (
    validate_idcard,
    validate_idcard_or_ruc,
    validate_ruc,
)


class IdcardField(CharField):
    def __init__(self, *args, **kwargs):
        max_length = validate_idcard.NUMBER_DIGITS
        kwargs.setdefault('max_length', max_length)
        kwargs.setdefault('validators', [validate_idcard, ])
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        form_class = FormIdcardField
        return super().formfield(form_class, **kwargs)


class RUCField(CharField):
    def __init__(self, *args, **kwargs):
        max_length = validate_ruc.NUMBER_DIGITS
        kwargs.setdefault('max_length', max_length)
        kwargs.setdefault('validators', [validate_ruc, ])
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        form_class = FormRUCField
        return super().formfield(form_class, **kwargs)


class IdcardOrRUCField(CharField):
    def __init__(self, *args, **kwargs):
        max_length = validate_ruc.NUMBER_DIGITS
        kwargs.setdefault('max_length', max_length)
        kwargs.setdefault('validators', [validate_idcard_or_ruc, ])
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        form_class = FormIdcardOrRUCField
        return super().formfield(form_class, **kwargs)
