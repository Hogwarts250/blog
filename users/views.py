from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import views as auth_views, logout

from blog_app.models import Topic

# Create your views here.
class LoginView(auth_views.LoginView):
    """Log the user in."""
    template_name = "users/login.html"
    topics = Topic.objects.order_by("text")
    extra_context = {"topics": topics}

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse("blog_app:home"))