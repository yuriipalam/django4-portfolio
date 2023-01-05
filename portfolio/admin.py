from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.auth.models import Group
from .models import Project, Introduction

from django import forms
from django.core.files.images import get_image_dimensions


class ProjectForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Project

    def clean_preview(self):
        preview = self.cleaned_data.get("preview")
        if not preview:
            raise forms.ValidationError("No image!")
        else:
            w, h = get_image_dimensions(preview)
            # if w != 528 and h != 326:
                # raise forms.ValidationError(
                    # "The image size supposed to be 528x326")
        return preview


class IntroductiomForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Introduction

    title = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 80, 'rows': 3}))


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm

    list_display = ("title", "get_preview_small")
    readonly_fields = ('get_preview_large', )
    change_form_template = 'admin/portfolio/project.html'

    def get_preview_small(self, obj):
        return mark_safe(f"<img src={obj.preview.url} width=110px>")
    get_preview_small.short_description = "Preview"

    def get_preview_large(self, obj):
        return mark_safe(f'<img src={obj.preview.url} width=300px style="margin-bottom: 10px;">')
    get_preview_large.short_description = "Example"

    def add_view(self, request, extra_context=None):
        self.fields = ('title', 'description', 'github', 'link', 'preview')
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.fieldsets = (
            (None,
             {
                 'fields': (('title', 'description', 'github', 'link'))
             }
             ),
            (None,
             {
                 'fields': (('preview', 'get_preview_large'),)
             })
        )
        return super().change_view(request, object_id)


class IntroductionAdmin(admin.ModelAdmin):
    form = IntroductiomForm
    readonly_fields = ('get_picture', )

    def get_picture(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width=300px style="margin-bottom: 10px;">')
    get_picture.short_description = "Preview"

    def add_view(self, request, extra_context=None):
        self.fields = ('title', 'description', 'picture', 'resume',)
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.fieldsets = (
            (None,
             {
                 'fields': (('title', 'description'))
             }
             ),
            (None,
             {
                 'fields': (('picture', 'get_picture'),)
             }),
            (None,
             {
                 'fields': (('resume',),)
             }),
        )
        return super().change_view(request, object_id)

    def has_add_permission(self, request):
        if Introduction.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if Introduction.objects.count() == 0:
            return False
        return super().has_change_permission(request, obj)
    
    def has_view_permission(self, request, obj=None):
        if Introduction.objects.count() == 0:
            return False
        return super().has_view_permission(request, obj)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Introduction, IntroductionAdmin)
admin.site.unregister(Group)

admin.site.site_title = "Portfolio Admin"
admin.site.site_header = "Portfolio Admin"
