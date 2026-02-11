from django import forms
from .models import Diary, Entry

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ["title"]

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["title", "content"]
