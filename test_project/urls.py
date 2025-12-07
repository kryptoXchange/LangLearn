
from django.contrib import admin
from django.urls import path

from accounts.views import home, lessons_view, signup_view, login_view, logout_view, coming_soon_view, lesson_uno_view

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('lessons/', lessons_view, name='lessons'),
    path('conversation-practice/', coming_soon_view, name='conversation-practice'),
    path('vocab-flashcards/', coming_soon_view, name='vocab-flashcards'),
    path('pronunciation-help/', coming_soon_view, name='pronunciation-help'),
    path('lesson-uno/', lesson_uno_view, name='lesson-uno'),

    path('admin/', admin.site.urls),
]
