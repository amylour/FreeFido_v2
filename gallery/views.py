from django.views.generic import TemplateView


class Gallery(TemplateView):
    template_name = 'gallery/gallery.html'
