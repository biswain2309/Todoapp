from django.contrib import admin
from django.urls import path
import notes.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', notes.views.home, name='home'),
    path('add/', notes.views.add, name='add'),
    path('delete/<int:todoapp_id>/', notes.views.delete, name='delete'),
    path('edit/<int:todoapp_id>/', notes.views.edit, name='edit'),
    path('update/<int:todoapp_id>', notes.views.update, name='update'),
]
