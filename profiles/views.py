from django.views.generic import TemplateView, UpdateView, DeleteView
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
        self.success_url = f'/profiles/user/{self.kwargs["pk"]}/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class ProfileDelete(DeleteView):
    """Delete profile view"""
    model = Profile
    template_name = 'profiles/delete_profile.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        # Get the user
        user = self.object.user

        # Delete the user's profile
        profile = self.object
        profile.delete()

        # Delete the user's articles
        Article.objects.filter(author=user).delete()

        # Delete the user's comments
        Comment.objects.filter(article__author=user).delete()

        # Delete the user's gallery images
        GalleryImage.objects.filter(photo_by=user).delete()

        # Delete the user's bookings
        Booking.objects.filter(user=user).delete()

        # Delete the user
        user.delete()

        messages.success(
            self.request, "Your profile and all associated data were deleted successfully.")
        return super().get_success_url()
