from django import forms

from To_Do_app.models import Tag, Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(attrs={"class": "datepicker", "type": "datetime-local"})
    )
    class Meta:
        model = Task
        fields = "__all__"