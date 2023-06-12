from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import GalleryImage
from .forms import GalleryImageForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

class Gallery(generic.ListView):
    model = GalleryImage
    queryset = GalleryImage.objects.order_by('-posted_on')
    template_name = 'gallery/gallery.html'
    paginate_by = 21
    context_object_name = 'gallery_posts'


class AddPhoto(LoginRequiredMixin, CreateView): 
    """ A view to upload an image """
    template_name = 'gallery/add_photo.html'
    model = GalleryImage
    form_class = GalleryImageForm
    success_url = '/gallery/'

    def form_valid(self, form):
        form.instance.photo_by = self.request.user
        return super().form_valid(form)

class DeletePhoto(DeleteView):
    """ Delete photo """
    model = GalleryImage
    success_url = '/gallery/'
    template_name = 'gallery/delete_photo.html'

    def test_func(self):
        return self.request.user == self.get_object().photo_by

    def delete(self, request, *args, **kwargs):
        photo = self.get_object()
        photo.delete()
        messages.success(request, "Photo deleted successfully.")
        return HttpResponseRedirect(self.success_url)
