from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from .models import Bike, Chainring, CassetteSprocket

from .forms import CadenceForm

import pdb

def index(request):
    bikes_list = Bike.objects.all()
    context = {'bikes_list': bikes_list}
    return render(request, 'bikes/index.html', context)

def about(request):
    return render(request, 'bikes/about.html')

def new(request):
    return render(request, 'bikes/new.html')

def add(request):
		bike = Bike(name = request.POST['name'], bike_make = request.POST['bike_make'], bike_model = request.POST['bike_model'], bike_type = request.POST['bike_type'], colour = request.POST['colour'], weight = request.POST['weight'], wheel_diameter = request.POST['wheel_diameter'])
		bike.save()
		return HttpResponseRedirect(reverse('bikes:show', args=(bike.id,)))

def edit(request, bike_id):
		bike = get_object_or_404(Bike, pk=bike_id)
		return render(request, 'bikes/edit.html', {'bike': bike})

def update(request, bike_id):
		bike = get_object_or_404(Bike, pk=bike_id)
		bike.name = request.POST['name']
		bike.bike_make = request.POST['bike_make']
		bike.bike_model = request.POST['bike_model']
		bike.bike_type = request.POST['bike_type']
		bike.colour = request.POST['colour']
		bike.weight = request.POST['weight']
		bike.wheel_diameter = request.POST['wheel_diameter']
		bike.save()
		return HttpResponseRedirect(reverse('bikes:show', args=(bike.id,)))

def show(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    chainrings_list = bike.chainring_set.all()
    cassettesprockets_list = bike.cassettesprocket_set.all()

    # if request.method == 'POST':
				# cadenceform = CadenceForm(request.POST)
				# if cadenceform.is_valid():
				# 		pdb.set_trace()
				# 		# process the data in form.cleaned_data  - this is an attribute. HOW?????????????????????????????????????  
    # else:
    # 		cadenceform = CadenceForm()

    ratio_matrix = []

    # Calculate the gear ratios
    for chainring in chainrings_list:
		    ratios = []
		    for cassettesprocket in reversed(cassettesprockets_list):
				    ratios.append(float(chainring.size) / float(cassettesprocket.size) * bike.wheel_diameter / 25.4)
		    ratio_matrix.append(ratios)

		# Calculate the speeds in km/h
    ratio_matrix2 = []

    if request.method == 'POST':
				cadenceform = CadenceForm(request.POST)
				if cadenceform.is_valid():
						for chainring in chainrings_list:
						    ratios = []
						    for cassettesprocket in reversed(cassettesprockets_list):
								    ratios.append(float(chainring.size) / float(cassettesprocket.size) * bike.wheel_diameter * 3.141 * float(cadenceform.cleaned_data['cadence']) * 60 / 1000 / 1000)
						    ratio_matrix2.append(ratios)  
    else:
    		cadenceform = CadenceForm()

    # for chainring in chainrings_list:
		  #   ratios = []
		  #   for cassettesprocket in reversed(cassettesprockets_list):
				#     ratios.append(float(chainring.size) / float(cassettesprocket.size) * bike.wheel_diameter * 3.141 * 90 * 60 / 1000 / 1000)
		  #   ratio_matrix2.append(ratios)

    return render(request, 'bikes/show.html', {'bike': bike, 'chainrings_list': chainrings_list, 'cassettesprockets_list': cassettesprockets_list, 'ratio_matrix': ratio_matrix, 'ratio_matrix2': ratio_matrix2, 'cadenceform': cadenceform })

def add_chainring(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    bike.chainring_set.create(size=request.POST['chainring'])
    return HttpResponseRedirect(reverse('bikes:show', args=(bike.id,)))

def add_cassettesprocket(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    bike.cassettesprocket_set.create(size=request.POST['cassettesprocket'])
    return HttpResponseRedirect(reverse('bikes:show', args=(bike.id,)))

def delete(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    bike.delete()
    return HttpResponseRedirect(reverse('bikes:index'))

    # try:
    #     bike.chainring_set.create(size=request.POST['chainring'])
    # except (KeyError, Chainring.DoesNotExist):
    #     return render(request, 'bikes/show.html', {
    #         'bike': bike,
    #         'error_message': "Chain ring was not created, please try again",
    #     })
    # else:
    #     return HttpResponseRedirect(reverse('bikes:show', args=(bike.id,)))