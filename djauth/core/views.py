#encoding=utf-8
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "core/index.html"


index = Index.as_view()