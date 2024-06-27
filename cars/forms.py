from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from cars.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class CarForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("view_counter",)
        # fields = "__all__"

    def clean_name(self):
        name_p = self.cleaned_data['name']
        if name_p in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            raise ValidationError('Запрещенные слова')
        return name_p

    def clean_description(self):
        descr_p = self.cleaned_data['description']
        if descr_p in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            raise ValidationError('Запрещенные слова')
        return descr_p


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
