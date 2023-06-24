import datetime

from django.core.exceptions import ValidationError


def dates_validator(dates):
    if len(dates) == 1:
        pass
    elif len(dates) == 2:
        if not dates[1] > dates[0]:
            raise ValidationError("Range date is not valid")
    else:
        raise ValidationError("Range date is not valid")


def valid_date(date):
    if date <= datetime.date.today():
        raise ValidationError("Date is not valid")
