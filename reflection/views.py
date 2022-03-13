from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ReflectionEntry
from .forms import FormReflectionOne, FormReflectionTwo

# Create your views here.

def reflection_formview(request):
    if request.method == 'POST':
        if request.POST.get('ReflectionForm2'):
            form1 = FormReflectionOne(request.POST)
            if form1.is_valid():
                request.session['Data_ReflectionForm1'] = form1.cleaned_data.get('feeling')
                if 'Data_ReflectionForm2' in request.session:
                    x = request.session['Data_ReflectionForm2']
                else:
                    x = None
                feeling = request.session['Data_ReflectionForm1']
                form2 = FormReflectionTwo(initial = x, feeling=feeling)
                adjective_choices = form2.get_adjectives(feeling=feeling)
                reason_choices = form2.get_reasons
                return render(request, 'reflection/form2.html', {'form2': form2, 'feeling': feeling, 'adjective_choices': adjective_choices, 'reason_choices':reason_choices})
            else:
                return render(request, 'reflection/form1.html', {'form1': form1})
        elif request.POST.get('ReflectionForm1'):
            form1 = FormReflectionOne()
            return render(request, 'reflection/form1.html', {'form1': form1})
        elif request.POST.get('submit'):
            form2 = FormReflectionTwo(feeling = request.session['Data_ReflectionForm1'], data=request.POST)
            if form2.is_valid() and request.user.is_authenticated:
                data_form2 = form2.cleaned_data
                feeling = request.session['Data_ReflectionForm1']
                adjective = data_form2.get('adjective')
                reason = data_form2.get('reason')
                ReflectionEntry.objects.create(
                    user=request.user,
                    feeling=feeling,
                    adjective=adjective,
                    reason=reason,
                )
            return redirect('dashboard')
                
    else:
        form1 = FormReflectionOne()
        return render(request, 'reflection/form1.html', {'form1': form1})

@login_required
def dashboard_view(request):
    reflections = ReflectionEntry.objects.filter(user=request.user)
    return render(request, 'reflection/dashboard.html', {'entries': reflections})
