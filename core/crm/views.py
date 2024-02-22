from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from crm import forms
from crm import models

# Create your views here.
@login_required
def list(request):
    people_list = models.Person.objects.all()
    return render(request, 'crm/list.html', {'people':people_list})

def person(request, person_id):
    person = get_object_or_404(models.Person, id = person_id)

    return render(request, 'crm/person.html', {'person':person})


def add_person(request):
    if request.method == 'POST':
        form = forms.AddpersonForm(request.POST)
        if form.is_valid():
            newperson = form.save()
            return redirect(newperson.get_absolute_url())
    else:
        form = forms.AddpersonForm()

    return render(request, 'crm/add.html', {'form':form})


def add_reason(request):
    if request.method == 'POST':
        form = forms.AddreasonForm(request.POST)
        if form.is_valid():
            newreason = form.save()
            return redirect('list')
    else:
        form = forms.AddreasonForm()

    return render(request, 'crm/addreson.html', {'form':form})

def reason(request, reason_id):
    reason = get_object_or_404(models.ReasonToVisit, id = reason_id)

    return render(request, 'crm/reason.html', {'reason':reason})

def edit_person(request, person_id):
    person = get_object_or_404(models.Person, id = person_id)
    if request.method == 'POST':
        form = forms.AddpersonForm(instance=person, data=request.POST)
        if form.is_valid():
            newperson = form.save()
            return redirect(newperson.get_absolute_url())
    else:
        form = forms.AddpersonForm(instance=person)

    return render(request, 'crm/add.html', {'form':form})


def edit_reason(request, reason_id):
    reason = get_object_or_404(models.ReasonToVisit, id = reason_id)
    if request.method == 'POST':
        form = forms.AddreasonForm(instance=reason, data=request.POST)
        if form.is_valid():
            newreason = form.save()
            return redirect(newreason.get_absolute_url())
    else:
        form = forms.AddreasonForm(instance=reason)

    return render(request, 'crm/add.html', {'form':form})