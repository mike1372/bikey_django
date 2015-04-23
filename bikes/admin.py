from django.contrib import admin

from .models import Bike, Chainring, CassetteSprocket

class ChainringInline(admin.TabularInline):
		model = Chainring
		extra = 0

class CassetteSprocketInline(admin.TabularInline):
		model = CassetteSprocket
		extra = 0

class BikeAdmin(admin.ModelAdmin):
		fieldsets = [
		  ('General Information', {'fields': ['name', 'bike_make', 'bike_model', 'bike_type', 'colour']}),
		  ('Technical information', {'fields': ['wheel_diameter', 'weight']}),
		]
		inlines = [ChainringInline, CassetteSprocketInline]
		list_display = ('name', 'bike_make', 'bike_model', 'bike_type', 'colour', 'wheel_diameter', 'weight')
		list_filter = ['bike_make', 'bike_type']
		search_fields = ['name', 'bike_make', 'bike_model', 'bike_type']

admin.site.register(Bike, BikeAdmin)