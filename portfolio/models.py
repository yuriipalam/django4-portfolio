from django.db import models
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField
from .storage import OverwriteStorage


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(max_length=1000, verbose_name="Description")
    preview = models.ImageField(
        upload_to='projects/previews', verbose_name="Preview image")
    github = models.URLField(
        blank=True, verbose_name="GitHub link (leave blank if none)")
    link = models.URLField(blank=False, verbose_name="Link to demo")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Introduction(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = HTMLField(max_length=2000, verbose_name="Description")
    picture = models.ImageField(
        upload_to='introduction/', verbose_name="Picture")
    resume = models.FileField(upload_to="introduction/", storage=OverwriteStorage(), max_length=100)

    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.get().id:
            raise ValidationError(
                f"Can create only 1 {model.__name__}'s instance")
        super().clean()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yurii Palamarchuk's Introduction"
        verbose_name_plural = "Yurii Palamarchuk's Introduction"
