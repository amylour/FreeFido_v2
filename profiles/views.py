from django.views.generic import TemplateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from allauth.account.views import LogoutView
from .models import Profile
from gallery.models import GalleryImage
from articles.models import Article, Comment
from booking.models import Booking
from .forms import ProfileForm


class ProfileView(TemplateView):
    """ Profile View """
    template_name = 'profiles/profile.html'

    def get_context_data(self, ** kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        bookings = profile.user.bookings.all()
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile),
            'bookings': bookings
        }

        return context


class ProfileEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ edit profile view """
    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.kwargs['pk']})

    def test_func(self):
        return self.request.user == self.get_object().user

 
