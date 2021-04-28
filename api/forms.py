from django.forms import ModelForm, ValidationError

from .models import GuideVersion


class GuideVersionAdminForm(ModelForm):
    class Meta:
        model = GuideVersion
        fields = ['name', 'guide', 'date_from']
        help_texts = {
            'name': 'Введите имя версии справочника',
            'guide': 'Выберите справочник (обязательное поле)',
            'date_from': 'Укажите дату начала действия версии'
        }

    def clean(self):
        name = self.cleaned_data.get('name')
        guide = self.cleaned_data.get('guide')
        if GuideVersion.objects.exclude(pk=self.instance.pk).filter(
                name=name, guide_unique=guide.id
        ).exists():
            raise ValidationError(f'Версия с именем {name} уже существует.')
        return self.cleaned_data
