from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField  # RichTextField yerine kullanacağız
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextUploadingField()  # RichTextField yerine RichTextUploadingField
    meta_description = models.CharField(max_length=160, blank=True)  # Meta açıklama alanı
    main_description = models.TextField(blank=True)  # Ana açıklama alanı
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
