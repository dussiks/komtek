import uuid

from django.db import models


class Guide(models.Model):
    id = models.UUIDField(
        'идентификатор',
        primary_key=True,
        default=uuid.uuid4(),
    )
    title = models.CharField('наименование', max_length=100)
    slug = models.SlugField('короткое наименование')
    description = models.TextField('описание')
    start_date = models.DateField('дата начала действия')
    version = models.CharField(
        max_length=5,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('title',)

    def versions(self):
        return GuideVersion.objects.filter(guide=self).order_by('-number')

    def save(self, *args, **kwargs):
        super(Guide, self).save(*args, **kwargs)
        guide_versions = self.check_versions()
        if self.version not in guide_versions:
            new_version = GuideVersion(
                guide=self,
                number=self.version,
                date_from = self.start_date,
            )
            new_version.save()


class GuideVersion(models.Model):
    number = models.DecimalField(
        'версия справочника',
        max_digits=2,
        decimal_places=1,
    )
    guide = models.ForeignKey(
        Guide,
        on_delete=models.CASCADE,
        related_name='versions',
        null=False,
        blank=False,
    )
    date_from = models.DateField()

    class Meta:
        unique_together = ('number', 'guide', )

    def __str__(self):
        return str(self.number)


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
