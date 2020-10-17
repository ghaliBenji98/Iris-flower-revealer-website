from django import forms

class FlowerForm(forms.Form):
	sepal_length=forms.FloatField (label='What is the length of the sepal in centimeters?')
	sepal_width=forms.FloatField (label='What is the width of the sepal in centimeters?')
	petal_length=forms.FloatField (label='What is the length of the petal in centimeters?')
	petal_width=forms.FloatField (label='What is the width of the petal in centimeters?')

