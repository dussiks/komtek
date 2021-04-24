import uuid

from django.db import models


class Guide(models.Model):
    id = models.UUIDField(
        'идентификатор',
        primary_key=True,
        default=uuid.uuid4(),
        editable=False,
    )
    title = models.CharField('наименование', max_length=100)
    slug = models.SlugField()
    description = models.TextField('описание')
    start_date = models.DateField('дата начала действия')
    version = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return '%s (%s)' % (self.id, self.title)


class Element(models.Model):
    guide = models.ForeignKey(
        Guide,
        on_delete=models.SET_NULL,
        related_name='elements',
        null=True,
    )
    code = models.CharField('код', max_length=50, null=False)
    value = models.CharField('значение', max_length=200, null=False)

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.code
