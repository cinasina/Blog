from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class TimeStampMixin(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class PublishPostManager(models.Manager):
#     get_queryset(self):
#         return super().get_queryset().filter(status = 'publish')

class Movies(TimeStampMixin):
    STATUS = (
        ('publish', 'Publish'),
        ('draft', 'Draft'),
    )
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    year = models.PositiveIntegerField()
    genres = models.CharField(max_length=70)
    director = models.CharField(max_length=70)
    stars = models.CharField(max_length=120)
    rate = models.FloatField(null=True, blank=True)
    storyline = RichTextUploadingField()
    certificate = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(choices=STATUS, default='draft', max_length=30)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('movie_details', args=[self.pk, self.slug])

    class Meta:
        verbose_name = 'Movie'



