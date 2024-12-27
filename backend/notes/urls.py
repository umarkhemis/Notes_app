from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesView.as_view(), name='create_and_view_notes'),
    path('notes/delete/<int:pk>', views.NoteDelete.as_view(), name='delete_note')
]
