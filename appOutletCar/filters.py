import django_filters
from .models import Coche

class FiltroCoches(django_filters.FilterSet):

	CHOICES = (
		('ascending', 'Ascending'),
		('descending', 'Descending')
	)

	ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

	class Meta:
		model = Coche
		fields= {
		'color':['icontains'],
		'anyo':['icontains'],
		'n_km':['icontains'],
		'potencia':['icontains']
		}

	def filter_by_order(self, queryset, name, value):
		expression = 'n_bastidor' if value == 'ascending' else '-n_bastidor'
		return queryset.order_by(expression).filter(estado="Segunda mano")

class FiltroCochesNuevos(django_filters.FilterSet):

	CHOICES = (
		('ascending', 'Ascending'),
		('descending', 'Descending')
	)

	ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

	class Meta:
		model = Coche
		fields= {
		'color':['icontains'],
		'anyo':['icontains'],
		'n_km':['icontains'],
		'potencia':['icontains']
		}

	def filter_by_order(self, queryset, name, value):
		expression = 'n_bastidor' if value == 'ascending' else '-n_bastidor'
		return queryset.order_by(expression).filter(estado="Nuevo")