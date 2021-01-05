from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
def employeeAdd(request):
    if request.method == 'POST':
        form = EmployeeAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empview')
    form = EmployeeAddForm()
    context = {'form': form }
    return render(request, 'employee-add.html', context)

def employeeView(request):
    employeeDetails = EmployeeAdd.objects.all()
    context = {'empdtl': employeeDetails}
    return render(request, 'employee-details.html', context)

def employeeEdit(request, pk):
    item = EmployeeAdd.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeAddForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('empview')
        return redirect("empedit")
    form = EmployeeAddForm(instance=item)
    context = {'form': form}
    return render(request, 'employee-edit.html', context)

def employeeDelete(request, pk):
    item = EmployeeAdd.objects.get(id=pk)
    # items = EmployeeAdd.objects.all()
    if request.method == 'POST':
        item.delete()
        return redirect('empview')

    context = {'item': item}
    return render(request, "delete-employee.html", context)

def render_pdf_view(request):
    template_path = 'all_employee.html'
    empdtl = EmployeeAdd.objects.all()
    context = {'employees': empdtl}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="employeedetails.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
