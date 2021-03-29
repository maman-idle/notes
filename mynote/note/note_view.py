from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.utils import timezone
from note.models import Note

# Create your views here.

#show note main menu
def notes(request):

    #get the last 3 notes 
    latest_notes_list = Note.objects.order_by('-note_date_created')[:3]
    context = {
        'latest_notes_list': latest_notes_list
        }

    if request.method == 'POST':
        #create a new note
        noteName = request.POST.get('noteName')
        noteDesc = request.POST.get('noteDesc')

        n = Note(note_name=noteName, note_desc=noteDesc, note_date_created=timezone.now(), note_status='False')
        n.save()
        return HttpResponseRedirect(reverse('note:notes'))
    
    else:
        return render(request, 'note/index.html', context)

def create(request):
    return render(request, 'note/create.html')

def editView(request, note_id):
    note = Note.objects.get(id=note_id)
    context = {
        'selected_note':note
    }
    return render(request, 'note/edit.html', context)

def edit(request, note_id):

    note = get_object_or_404(Note, pk=note_id)

    noteName = request.POST.get('newNoteName')
    noteDesc = request.POST.get('newNoteDesc')
    
    editedNote = Note.objects.filter(pk=note_id).update(note_name=noteName, note_desc=noteDesc, note_date_created=timezone.now())

    return HttpResponseRedirect(reverse('note:notes'))

def delete(request, note_id):
     note = get_object_or_404(Note, pk=note_id)

     note.delete()
     return HttpResponseRedirect(reverse('note:notes'))

def showAll(request):
    list_notes = Note.objects.order_by('-note_date_created')

    context = {
        'list_notes' : list_notes
    }

    return render(request, 'note/allNotes.html', context)