from django.db import models


class Guide(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField('наименование', max_length=100)
    slug = models.SlugField()
    description = models.TextField('описание')
    start_date = models.DateTimeField('дата начала действия')
    version = models.CharField(unique=True, null=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Element(models.Model):
    guide = models.ForeignKey(
        Guide,
        on_delete=models.CASCADE,
        related_name='elements',
        blank=False,
        null=False,
    )
    code = models.CharField('код', null=False)
    value = models.CharField('значение', null=False)

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.code
