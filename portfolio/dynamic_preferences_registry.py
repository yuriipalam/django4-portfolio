from dynamic_preferences.types import StringPreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from django import forms
from django.forms import ValidationError

portfolio = Section('general')


@global_preferences_registry.register
class SiteGitHub(StringPreference):
    field_class = forms.URLField
    field_kwargs = {
        'widget': forms.TextInput(attrs={'size': '60'}),
    }
    section = portfolio
    name = 'github_link'
    default = 'None'
    required = True
    verbose_name = "GitHub Profile Link"


@global_preferences_registry.register
class SiteFreelancer(StringPreference):
    field_class = forms.URLField
    field_kwargs = {
        'widget': forms.TextInput(attrs={'size': '60'}),
    }
    section = portfolio
    name = 'freelancer_link'
    default = 'None'
    required = True
    verbose_name = "Freelancer Profile Link"


@global_preferences_registry.register
class SiteLinkedIn(StringPreference):
    field_class = forms.URLField
    field_kwargs = {
        'widget': forms.TextInput(attrs={'size': '60'}),
    }
    section = portfolio
    name = 'linkedin_link'
    default = 'None'
    required = True
    verbose_name = "LinkedIn Profile Link"


@global_preferences_registry.register
class SiteMetaDescription(StringPreference):
    field_class = forms.CharField
    field_kwargs = {
        'widget': forms.widgets.Textarea({'cols': 80, 'rows': 15}),
    }
    section = portfolio
    name = 'meta_description'
    default = 'None'
    required = True
    verbose_name = "Description Meta Tag"

    def validate(self, value):
        if len(value) > 500:
            raise ValidationError(
                "Length shouldn't be more than 500 characters")


@global_preferences_registry.register
class SiteTitle(StringPreference):
    field_class = forms.CharField
    field_kwargs = {
        'widget': forms.TextInput(attrs={'size': '60'}),
    }
    section = portfolio
    name = 'title'
    default = 'Yurii Palamarchuk - Portfolio'
    required = True
    verbose_name = "Website Title"

    def validate(self, value):
        if len(value) > 100:
            raise ValidationError(
                "Length shouldn't be more than 100 characters")
