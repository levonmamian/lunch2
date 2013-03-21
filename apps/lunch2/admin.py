from lunch2.models import Restaurant, Item, ItemType, MealOrder, PersonalOrder
from django.contrib import admin

class ItemInLine(admin.TabularInline):
	model = Item
	extra = 15

class ItemTypeInLine(admin.TabularInline):
	model = ItemType
	extra = 3

class RestaurantAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ('name', 'address', 'website')}),
	]
	inlines = (ItemTypeInLine, ItemInLine,)

class MealOrderAdmin(admin.ModelAdmin):
	fields = ('restaurant', 'date', 'limit', 'time_deadline')
	list_filter = ['time_deadline', 'date']

class PersonalItemInLine(admin.TabularInline):
	model = PersonalOrder.items.through

class PersonalOrderAdmin(admin.ModelAdmin):
	fields = ('mealorder', 'user')
	inlines = (PersonalItemInLine,)
	#list_filter = 

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(MealOrder, MealOrderAdmin)
admin.site.register(PersonalOrder, PersonalOrderAdmin)