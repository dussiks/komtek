import uuid

from django.db import models


class Guide(models.Model):
    id = models.UUIDField(
        'идентификатор',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
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

    def check_versions(self):
        return GuideVersion.objects.filter(guide=self)

    def save(self, *args, **kwargs):
        super(Guide, self).save(*args, **kwargs)
        new_guide_version = GuideVersion(
            guide=self,
            name=self.version,
            date_from=self.start_date,
            guide_unique=self.id,
        )
        new_guide_version.save()


class GuideVersion(models.Model):
    name = models.CharField(
        'версия справочника',
        max_length=5,
        null=False,
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
        max_length=64,
    )
    date_from = models.DateField('дата начала действия')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        current_guide_versions = self.guide.check_versions()
        versions_list = [x.name for x in current_guide_versions]
        if self.name not in versions_list:
            self.guide_unique = self.guide.id
            super().save(*args, **kwargs)


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
