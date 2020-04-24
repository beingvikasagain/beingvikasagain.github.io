from django.shortcuts import render
from basicapp.forms import MyForm,MyModelForm
from basicapp.models import MyModel

# Create your views here.
def index(request):
    model = MyModel.objects.order_by('name')


    form = MyForm
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['roll_no'])


    return render(request,'basicapp/index.html',{'insert_form':form,'data':model})


def form_view(request):
    modelform = MyModelForm
    if request.method=='POST':
        modelform = MyModelForm(request.POST)
        if modelform.is_valid():
            print("Validation Successful!")
            modelform.save(commit=True)
        else:
            print("Error! Form Invalid...")
    return render(request,'basicapp/forms.html',{'insert_modelform':modelform})
