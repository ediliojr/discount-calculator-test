from django import forms

class InvestmentForm(forms.Form):
	# starting_amount
	valor1= forms.FloatField()
	valor2= forms.FloatField()
	valor3= forms.FloatField()
	tarifa = forms.FloatField()
	tipo_tarifa = forms.CharField()