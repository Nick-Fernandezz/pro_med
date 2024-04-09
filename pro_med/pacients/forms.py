from django import forms
from . models import TherapeuticAndDiagnosticEvents

class TherapeuticAndDiagnosticEventsForm(forms.ModelForm):
    class Meta:
        model = TherapeuticAndDiagnosticEvents
        fields = ('type', 'event_name', 'event_result', 'diagnos', 'recomendations')


class CreateHospitalizationForm(forms.Form):
    def __init__(self, pacient_id):

        td_events = TherapeuticAndDiagnosticEvents.objects.filter(pacient__id=pacient_id).order_by('-started_date')[:20]
        self.codes = []
        for event in td_events:
            self.codes.append((event.id, f'{event.doctor.last_name} {event.diagnos}'))
        print(self.codes)
        
    pacient = forms.HiddenInput()
    created_by = forms.HiddenInput()
    code = forms.IntegerField(label="Код приема, назначающего госпитализацию")
    code = forms.CharField(
        widget=forms.Select(choices=codes)
    )
    datetime = forms.DateTimeField(label="Дата и время госпитализации", 
                                widget=forms.DateTimeInput({'type': 'datetime-local'}))


