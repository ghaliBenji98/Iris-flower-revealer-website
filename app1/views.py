from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from . forms import FlowerForm
from django.contrib import messages
from . models import flowerDim
from . serializers import FlowerSerializers
import joblib
import pandas as pd



class FlowerView(viewsets.ModelViewSet):
        queryset = flowerDim.objects.all()
        serializer_class = FlowerSerializers


def Predict(unit):
	model = joblib.load('C:/Users/hamea/OneDrive/Bureau/model/mysite/app1/mlp_classifier.jbl')
	y_pred=model.predict(unit)
	newdf=pd.DataFrame(y_pred, columns=['Class'])
	newdf=newdf.replace({0:'Iris-setosa', 1:'Iris-versicolor', 2:'Iris-virginica'})
	return newdf.values[0][0]
	


def flowerNature(request):
        if request.method=='POST':
                form=FlowerForm(request.POST)
                if form.is_valid():
                        sepal_length = form.cleaned_data['sepal_length']
                        sepal_width = form.cleaned_data['sepal_width']
                        petal_length = form.cleaned_data['petal_length']
                        petal_width = form.cleaned_data['petal_width']
                        myDict = (request.POST).dict()
                        Input = list(myDict.values())
                        Input = [float(string) for string in Input[1:]]    
                        Output = Predict([Input])
                        messages.success(request,'Flower Nature: {}'.format(Output))

                       
        form=FlowerForm()
        return render(request, 'cxform.html', {'form':form})

