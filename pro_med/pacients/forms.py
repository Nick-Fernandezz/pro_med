from django import forms
from . models import TherapeuticAndDiagnosticEvents

class TherapeuticAndDiagnosticEventsForm(forms.ModelForm):
    class Meta:
        model = TherapeuticAndDiagnosticEvents
        fields = ('type', 'event_name', 'event_result', 'diagnos', 'recomendations')


class CreateHospitalizationForm(forms.Form):
    
    pacient = forms.HiddenInput()
    created_by = forms.HiddenInput()
    code = forms.CharField(label="Код приема, назначающего госпитализацию")
    datetime = forms.DateTimeField(label="Дата и время госпитализации", 
                                widget=forms.DateTimeInput({'type': 'datetime-local'}))
    
    


