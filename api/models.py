from datetime import date
from django.db import models

from django.utils.functional import cached_property


class Guide(models.Model):
    """
    At first Guide object creation automatically save first default version
    for current object with version name 1.0.0.
    """
    title = models.CharField('наименование справочника', max_length=100)
    slug = models.SlugField('короткое наименование', max_length=30, unique=True)
    description = models.TextField('описание', null=True)

    @cached_property
    def version(self):
        versions = self.versions
        if versions:
            return versions.latest().name

    @cached_property
    def start_date(self):
        return self.versions.latest().date_from

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        is_new = True if not self.id else False
        super().save(*args, **kwargs)
        if is_new:
            GuideVersion.objects.create(
                name='1.0.0',
                guide=self,
                guide_unique=self.id,
                date_from=date.today(),
            )


class GuideVersion(models.Model):
    """
    Edition of current GuideVersion object except in Django Admin form will
    cause IntegrityError because if UniqueConstraint condition. If other
    interface for edition will be necessary - validation of input fields
    should be provided to avoid exception.
    """
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
        max_length=32,
        null=True,
        blank=True,
    )
    date_from = models.DateField('дата начала действия')

    class Meta:
        get_latest_by = 'date_from'
        constraints = [
            models.UniqueConstraint(
                fields=['guide_unique', 'name'],
                name='unique_guide_version'
            )
        ]

    def __str__(self):
        return f'{self.guide} v.{self.name}'

    def save(self, *args, **kwargs):
        self.guide_unique = self.guide.id
        super().save(*args, **kwargs)


class Element(models.Model):
    code = models.CharField('код', max_length=50)
    value = models.CharField('значение', max_length=200)
    version = models.ManyToManyField(
        GuideVersion,
        verbose_name='версия справочника',
        help_text='Выберите версии справочников для элемента.',
        related_name='elements',
        blank=True,
    )

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.code
