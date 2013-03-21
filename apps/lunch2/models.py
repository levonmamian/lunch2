from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	website = models.URLField(max_length=200)

	def __unicode__(self):
		return self.name

class ItemType(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200, default="")
	restaurant = models.ForeignKey(Restaurant)

	def __unicode__(self):
		return self.restaurant.name +": " + self.name

class MealOrder(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	time_deadline = models.DateTimeField('Deadline for Order')
	date = models.DateField('Order Date')
	limit = models.DecimalField('Price Limit', max_digits=6, decimal_places=2, default = 25.00)

	def isOpenOrder(self):
		return time_deadline >= timezone.now()

	def totalCost(self):
		p = PersonalOrder.objects.filter(mealorder = self)
		cost = 0
		for order in p:
			cost = cost + order.totalcost
		return cost

	def relatedPersonalOrders(self):
		return PersonalOrder.objects.filter(mealorder = self)

	def allItems(self):
		d = {}
		p = self.relatedPersonalOrders()
		for order in p:
			for item in order.items.all():
				if item in d:
					d[item] = d[item] + MultipleItems.objects.filter(personalorder = order, item = item)[0].num_items
				else:
					d[item] = MultipleItems.objects.filter(personalorder = order, item = item)[0].num_items
		return d


	def __unicode__(self):
		return self.restaurant.name + " " + unicode(self.date.month) + "/" + unicode(self.date.day) + "/" + unicode(self.date.year)

class Item(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	itemtype = models.ForeignKey(ItemType)
	restaurant = models.ForeignKey(Restaurant)
	
	def __unicode__(self):
		return self.restaurant.name + ": " + self.itemtype.name + " - " + self.name

class PersonalOrder(models.Model):
	mealorder = models.ForeignKey(MealOrder)
	user = models.ForeignKey(User)
	items = models.ManyToManyField(Item, through='MultipleItems')
	totalcost = models.DecimalField(max_digits=6, decimal_places=2)
	comment = models.CharField(max_length=300, default="")

	def __unicode__(self):
		return self.user.username + ": " + self.mealorder.__unicode__()

class MultipleItems(models.Model):
	personalorder = models.ForeignKey(PersonalOrder)
	item = models.ForeignKey(Item)
	num_items = models.IntegerField()

def newUser(username, email, password):
	user = User.objects.create_user(username, email, password)

def changePassword(username, password):
	u = User.objects.get(username__exact=username)
	u.set_password(password)
	u.save()

def isValidUsername(field_data):
	if field_data == '' or len(field_data.encode('ascii','ignore')) < 3:
		return False
	try:
		User.objects.get(username = field_data)
	except User.DoesNotExist:
		return True
	return False

def isValidEmail(field_data):
	try:
		User.objects.get(email = field_data)
	except User.DoesNotExist:
		return True
	return False


















