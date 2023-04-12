from django.shortcuts import render
from django.views import View
from .forms import InvestmentForm

class Index(View):
	def get(self, request):
		form = InvestmentForm()
		return render(request, 'calculator/index.html', {'form': form})

	def post(self, request):
		form = InvestmentForm(request.POST)
		desconto=1

		if form.is_valid():
			
			valor1 = form.cleaned_data['valor1']
			valor2 = form.cleaned_data['valor1']
			valor3 = form.cleaned_data['valor1']
			tarifa = form.cleaned_data['tarifa']
			tipo_tarifa = form.cleaned_data['tipo_tarifa']
			resultados = [0,0,0,0,0,0]
			consumo_medio = (valor1 + valor2 + valor3) / 3

			if consumo_medio < 10000:
				if tipo_tarifa == 'Residencial':
					desconto = 0.18
				elif tipo_tarifa == 'Comercial':
					desconto = 0.16
				elif tipo_tarifa == 'Industrial':
					desconto = 0.12
			elif consumo_medio >= 10000 and consumo_medio <= 20000:
				if tipo_tarifa == 'Residencial':
					desconto = 0.22
				elif tipo_tarifa == 'Comercial':
					desconto = 0.18
				elif tipo_tarifa == 'Industrial':
					desconto = 0.15
			else:
				if tipo_tarifa == 'Residencial':
					desconto = 0.25
				elif tipo_tarifa == 'Comercial':
					desconto = 0.22
				elif tipo_tarifa == 'Industrial':
					desconto = 0.18

			economia_anual = (valor1 + valor2 + valor3) * tarifa * desconto * 12
			
			# Calcular a economia mensal
			economia_mensal = economia_anual / 12
			
			# Calcular a cobertura
			if consumo_medio < 10000:
				cobertura = 0.9
			elif consumo_medio >= 10000 and consumo_medio <= 20000:
				cobertura = 0.95
			else:
				cobertura = 0.99
			
			# Calcular o valor coberto
			valor_coberto = (valor1 + valor2 + valor3) * cobertura
			
			resultados[0] = round(economia_anual, 2)
			resultados[1] = round(economia_mensal, 2)
			resultados[2] = round(desconto, 2)
			resultados[3] = round(valor_coberto, 2)

			# Retornar os resultados como um dicionário
			context = {
				'economia_anual': economia_anual,
				'economia_mensal': economia_mensal,
				'desconto_aplicado': desconto,
				'cobertura': cobertura,
				'valor_coberto': valor_coberto
		}

			# for i in range(1, int(form.cleaned_data['number_of_years'] + 1)):
			# 	yearly_results[i] = {}

			# 	# calculate the interest
			# 	interest = total_result * (form.cleaned_data['return_rate'] / 100)
			# 	total_result += interest
			# 	total_interest += interest

			# 	# add additional contribution
			# 	total_result += form.cleaned_data['annual_additional_contribution']

			# 	# set yearly_results
			# 	yearly_results[i]['interest'] = round(total_interest, 2)
			# 	yearly_results[i]['total'] = round(total_result, 2)

			# 	# create context
				# context = {
				# 	'total_result': round(total_result, 2),
				# 	'yearly_results': yearly_results,
				# 	'number_of_years': int(form.cleaned_data['number_of_years'])
				# }

		



		# render the template
		return render(request, 'calculator/result.html', context)