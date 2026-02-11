from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Diary, Entry
from .forms import DiaryForm, EntryForm

@login_required
def diary_list(request):
    diaries = Diary.objects.filter(user=request.user)
    return render(request, "dairy/diary_list.html", {"diaries": diaries})

@login_required
def diary_detail(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, user=request.user)
    entries = diary.entries.all()
    return render(request, "dairy/diary_detail.html", {"diary": diary, "entries": entries})

@login_required
def add_diary(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect("diary_list")
    else:
        form = DiaryForm()
    return render(request, "dairy/add_diary.html", {"form": form})

@login_required
def add_entry(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, user=request.user)
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.diary = diary
            entry.save()
            return redirect("diary_detail", diary_id=diary.id)
    else:
        form = EntryForm()
    return render(request, "dairy/add_entry.html", {"form": form, "diary": diary})
