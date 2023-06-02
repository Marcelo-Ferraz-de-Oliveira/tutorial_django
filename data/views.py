from django import forms
from django.shortcuts import render
from django.utils.safestring import mark_safe

from datetime import datetime
import subprocess

class MudarDataForm(forms.Form):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label=mark_safe(f'Informe a nova data:'))

def data(request):
    if request.method == 'POST':
        form = MudarDataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            data_formatada = f'{data.year}-{data.month}-{data.day}'
            hora_atual = datetime.now()
            hora_formatada = f'{hora_atual.hour}:{hora_atual.minute}:{hora_atual.second}'
            print(hora_formatada)
            comando = f"timedatectl set-ntp no & timedatectl set-time '{data_formatada} {hora_formatada}'"
            subprocess.run(comando, shell=True)
            return render(request, 'data/data.html', {'form': form})
    else:
        form = MudarDataForm()
    return render(request, 'data/data.html', {'form': form})