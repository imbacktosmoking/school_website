from django.contrib import admin
from django.urls import path, include
from main.views import RegistrationView, Homepage, Physics, Details, create_post, CategoryDetailView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('details/<int:pk>', Details.as_view(), name="details"),
    path('category/<int:pk>', CategoryDetailView.as_view(), name="category"), 
    path('physics/', Physics.as_view(), name="physics"),
    path('post/', create_post, name="post"),
    path('', Homepage.as_view(), name="homepage"),
    path('users/', include("django.contrib.auth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
