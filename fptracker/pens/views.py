from django.shortcuts import render, redirect
from pens.models import Pen, Ink
from pens.forms import PenForm, InkForm

# Create your views here.

def index(request, pen_brand = None, current_ink = None):

    pens = Pen.objects.all()
    if pen_brand is not None:
        pens = pens.filter(brand_name = pen_brand)

    
    if current_ink is not None:
        pens = pens.filter(current_ink_id = current_ink)

    ink = Ink.objects.filter(id = current_ink).first()
    all_inks = Ink.objects.all()

    if request.user.is_authenticated:
        pen_ids = request.user.profile.pens.values_list('id',flat = True)
    else:
        pen_ids = None

    context = {
        'pen_list': pens,
        'ink_list': all_inks,
        'pen_brand':pen_brand,
        'current_ink':current_ink,
        'current_ink_name': ink,
        'pen_ids':pen_ids,
        'page_title':'Fountain pen collection'
    }
    return render(request, "index.html",context)

def edit_pen(request, pen_id = None):

    if request.method == "POST":

        if pen_id is not None:
            pen = Pen.objects.get(id = pen_id)
            form = PenForm(request.POST, instance = pen)
        else:
            form = PenForm(request.POST)

        if form.is_valid():
            updated_pen = form.save(commit = False)
            updated_pen.added_by = request.user.profile
            updated_pen.save()
            return redirect(index)
    else:

        if pen_id is not None:
            pen = Pen.objects.get(id = pen_id)
            form = PenForm(instance = pen)
        else:
            form = PenForm()
    
    context = {
        'form':form,
        'obj_id':pen_id,
        'obj_type': 'Pen'

    }
    return render(request,"edit_object.html",context)


def delete_pen(request, pen_id):
    pen = Pen.objects.get(id = pen_id)
    pen.delete()
    return redirect(index)


def edit_ink(request, ink_id=None):
    if request.method == "POST":
        if ink_id is not None:
            ink = Ink.objects.get(id = ink_id)
            form = InkForm(request.POST, instance = ink)
        else:
            form = InkForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(index)

    else:
        if ink_id is not None:
            ink = Ink.objects.get(id = ink_id)
            form = InkForm(instance = ink)
        else:
            form = InkForm()
    
    context = {
        'form': form,
        'obj_id' :ink_id,
        'obj_type': 'Ink'
    }

    return render(request, 'edit_object.html', context)


def delete_ink(request, ink_id):
    ink = Ink.objects.get(id = ink_id)
    ink.delete()
    return redirect(index)