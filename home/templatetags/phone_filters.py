from django import template
import re

from django import template
import re


register = template.Library()


@register.filter(name='phone_link')
def phone_link(value):
    """
    Преобразует телефонный номер в формат для ссылки tel:
    Примеры:
    +7 (999) 123-45-67 -> +79991234567
    8(999)123-45-67 -> +79991234567
    89991234567 -> +79991234567
    """
    phone = re.sub(r'\D', '', str(value))
    
    if len(phone) == 11:
        if phone.startswith('8') or phone.startswith('7'):
            phone = '+7' + phone[1:]
    elif len(phone) == 10:
        phone = '+7' + phone
        
    return phone

