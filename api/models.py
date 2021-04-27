from django.db import models
from django.db import IntegrityError


class Guide(models.Model):
    title = models.CharField('наименование', max_length=100)
    slug = models.SlugField('короткое наименование')
    description = models.TextField('описание', null=True)
    start_date = models.DateField('дата начала действия')

    @property
    def version(self):
        return self.versions.last()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        is_new = True if not self.id else False
        super().save(*args, **kwargs)
        if is_new:
            GuideVersion.objects.create(
                name='1.0.0',
                guide=self,
                guide_unique=self.id,
                date_from=self.start_date,
            )


class GuideVersion(models.Model):
    name = models.CharField(
        'версия справочника',
        max_length=10,
        blank=False,
    )
    guide = models.ForeignKey(
        Guide,
        verbose_name='наименование справочника',
        on_delete=models.CASCADE,
        related_name='versions',
        null=False,
        blank=False,
    )
    guide_unique = models.CharField(
        'идентификатор справочника',
        help_text='(оставьте пустым, заполнится автоматически)',
        max_length=32,
        null=True,
        blank=True,
    )
    date_from = models.DateField('дата начала действия')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['guide_unique', 'name'], name='unique guideversion')
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.guide_unique = self.guide.id
        if GuideVersion.objects.filter(guide_unique=self.guide_unique, name=self.name).exists():
            return f'Версия {self.name} уже существует. Укажите новое имя для версии.'
        else:
            super().save(*args, **kwargs)


class Element(models.Model):
    code = models.CharField('код', max_length=50)
    value = models.CharField('значение', max_length=200)
    version = models.ManyToManyField(
        GuideVersion,
        verbose_name='версия справочника',
        related_name='elements',
        blank=True,
    )

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.code
