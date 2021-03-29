from django.urls import path
from .import note_view
from django.urls import include

app_name = 'note'
urlpatterns = [
    path('', note_view.notes, name='notes'),
    path('create', note_view.create, name='create_note'),
    path('edit/<int:note_id>', note_view.editView, name='edit_note'),
    path('edit/<int:note_id>/note', note_view.edit, name='edit_finish'),
    path('delete/<int:note_id>', note_view.delete, name='delete_note'),
    path('all', note_view.showAll, name='show_all'),
]
