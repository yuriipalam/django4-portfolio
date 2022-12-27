from .models import Introduction
from django.http import Http404

def add_variable_to_context(request):
    try:
        resume_url = Introduction.objects.get().resume.url
    except Introduction.DoesNotExist:
        return ""
    return {
        'resume_url': resume_url,
    }