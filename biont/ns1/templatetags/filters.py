from django import template
import re
# from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='page')
def page(request, p):
	get = request.GET.copy()
	get['page'] = p

	return "?"+get.urlencode()

@register.filter(name='sppage')
def page(request):
	url = request.path.split("?")[0]
	return url

@register.filter(name='sp1')
def sp1(request,taxonomic):
	result = ""
	if taxonomic:
		result = taxonomic.split(" ")[0]
	return result

@register.filter(name='sp2')
def sp2(request,taxonomic):
	result = ""
	if len(taxonomic.split(" "))>1:
		result = taxonomic.split(" ")[1]
	return result

@register.filter(name='getlen')
def getlen(request,Protein_attributes):
	result = ""
	if Protein_attributes:
		result = Protein_attributes.split(":")[1].strip()[:3]
	return result

@register.filter(name='is_selected')
def is_selected(from_id, to_id):
	result = ""	
	if from_id == str(to_id):
		result = "selected"
	return result

@register.filter(name="get_field")
def get_field(request, field):
	return request.GET.get(field)

@register.filter(name="near_range")
def near_range(pagination):
	half_range = 3
	current = pagination.number
	start = current-half_range
	if start<1:
		start = 1
	end = current+half_range
	if end>pagination.paginator.num_pages:
		end = pagination.paginator.num_pages

	return range(start, end+1)

@register.filter(name="none_2_null")
def none_2_null(str):
	result = str
	if (not str) or str.lower()=="none":
		result = ""
	return result

@register.filter(name="enum")
def enum(arr):

	return enumerate(arr)