from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from lunch2.models import Restaurant, Item, MealOrder, ItemType, PersonalOrder, MultipleItems, isValidUsername, isValidEmail

#View for the home page. 
def home(request):
	open_mealorders = MealOrder.objects.all().filter(time_deadline__gte = timezone.now())
	closed_mealorders = MealOrder.objects.all().filter(time_deadline__lt = timezone.now())[0:10]
	restaurant_list = Restaurant.objects.all().order_by('name')
	username = request.user.username
	return render_to_response('home.html', 
		{'restaurant_list': restaurant_list, 'open_mealorders' : open_mealorders, 'closed_mealorders' : closed_mealorders, 
		'username' : username, }, context_instance=RequestContext(request))

#View for the page showing all restaurants
def allrestaurants(request):
	restaurant_list = Restaurant.objects.all().order_by('name')
	return render_to_response('restaurantlist.html', {'restaurant_list': restaurant_list}, context_instance=RequestContext(request))

#View for the page showing all restaurants
def allmealorders(request):
	mealorder_list = MealOrder.objects.all().order_by('-time_deadline')
	return render_to_response('mealorderlist.html', {'mealorder_list': mealorder_list}, context_instance=RequestContext(request))

#View for the restaurant detail page
def restaurantdetail(request, restaurant_id):
	r = get_object_or_404(Restaurant, pk=restaurant_id)
	return render_to_response('restaurantdetail.html', {'restaurant' : r}, context_instance=RequestContext(request))

#View for the meal order detail page
@login_required
def mealorderdetail(request, mealorder_id):
	m = get_object_or_404(MealOrder, pk=mealorder_id)
	return render_to_response('mealorderdetail.html', {'mealorder' : m}, context_instance=RequestContext(request))

#Initial Login Screen
def login(request):
	return render_to_response('login.html', {}, context_instance=RequestContext(request))

#Response to a login request
def login_post(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('/lunch2/')
        else:
            return render_to_response('error.html', {}, context_instance=RequestContext(request))
    else:
    	message = "Login failed. Please try again."
        return render_to_response('login.html', {'message' : message}, context_instance=RequestContext(request))

#Logout request
def logout_view(request):
    logout(request)
    return redirect('/lunch2/')

#Registration request for new user
def register(request):
	return render_to_response('registration.html', {}, context_instance=RequestContext(request))

#Posting a registration request
def register_post(request):
	if request.user.is_authenticated():
		message = "Account already exists!"
		return render_to_response('registration.html', {'message' : message},  context_instance=RequestContext(request))
	username = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	passwordcheck = request.POST['password2']
	if not isValidUsername(username):
		message = "Username %s already exists or is too short, please choose a new one (3 characters or more)." % username
		return render_to_response('registration.html', {'message' : message},  context_instance=RequestContext(request))
	if not isValidEmail(email):
		message = "Email %s is already registered, please use a new email or login." % email
		return render_to_response('registration.html', {'message' : message},  context_instance=RequestContext(request))
	if not passwordcheck == password:
		message = "Passwords did not match, please try again."
		return render_to_response('registration.html', {'message' : message},  context_instance=RequestContext(request))
	user = User.objects.create_user(username, email, password)
	user.backend='django.contrib.auth.backends.ModelBackend'
	user.save()
	authenticate(username=username, password=password)
	auth_login(request, user)
	return redirect('/lunch2/')

#Request to reset password
def resetpassword(request):
	return render_to_response('resetpassword.html', {}, context_instance=RequestContext(request))

#Processing reset password request:
def resetpassword_post(request):
	message = ""
	email = request.POST['email']
	password = request.POST['password']
	if isValidEmail(email):
		message = "That is not a valid email. Please register."
		return render_to_response('resetpassword.html', {'message': message }, context_instance=RequestContext(request))
	if password != request.POST['password2']:
		message = "Those passwords do not match. Please try again."
		return render_to_response('resetpassword.html', {'message': message }, context_instance=RequestContext(request))
	if request.user.is_authenticated() and email == request.user.email:
		request.user.password = password
		message = "Password reset successfully for existing user %s" % request.user.username
		return render_to_response('resetpassword.html', {'message': message }, context_instance=RequestContext(request))
	elif request.user.is_authenticated() and request.user.email != email:
		message = "You are logged in with a different email address. Please either logout first or check the email address."
		return render_to_response('resetpassword.html', {'message': message }, context_instance=RequestContext(request))
	else:
		user = User.objects.get(email = email)
		user.password = password
		user.backend='django.contrib.auth.backends.ModelBackend'
		user.save()
		auth_login(request, user)
		message = "Password reset successfully! You are now logged in %s." % user.username
	return render_to_response('resetpassword.html', {'message': message }, context_instance=RequestContext(request))

#View for the stats on a past meal order
def pastmealorder(request, mealorder_id):
	m = get_object_or_404(MealOrder, pk=mealorder_id)
	if not m:
		raise Http404
	cost = m.totalCost()
	p = m.relatedPersonalOrders() #all personal orders that are part of this meal order
	itemdict = m.allItems() #Dictionary from item in restaurant to total number of that item over all orders
	d = {} # Dictionary from personalorder : { item : num of item }
	for order in p:
		d2 = {}
		for item in order.items.all():
			d2[item] = item.multipleitems_set.get(personalorder = order).num_items
		d[order] = d2
	return render_to_response('pastmealorder.html', {'mealorder' : m, 'cost' : cost, 'relatedpersonalorders' : p, 
		'itemdict' : itemdict, 'allpeople' : d}, context_instance=RequestContext(request))

#What happens when someone submits an order
@login_required
def enterorder(request, mealorder_id):
	order = get_object_or_404(MealOrder, pk=mealorder_id)
	user = request.user
	if order.time_deadline <= timezone.now():
		return redirect('/lunch2/mealorder/(?P<mealorder_id>\d+)/summary/')
	
	itemtypecounter = 0
	itemcounter = 0
	totalprice = 0
	personalorderitems = {}
	for itemtype in order.restaurant.itemtype_set.all():
		itemtypecounter = itemtypecounter + 1
		for item in itemtype.item_set.all():
			itemcounter= itemcounter + 1
			itemname = 'item' + str(itemtypecounter) + str(itemcounter)
			numofthisitem = int(request.POST[itemname])
			totalprice = totalprice + (numofthisitem * item.price)
			if numofthisitem > 0:
				personalorderitems[item] = numofthisitem
		itemcounter = 0
	if totalprice > order.limit:
		message = "Your order exceeded the price limit set. Please try again."
		return render_to_response('mealorderdetail.html', {'mealorder' : order, 'message' : message},
		context_instance=RequestContext(request))
	comment = request.POST['comment']
	previouspersonalorder = PersonalOrder.objects.filter(user = user, mealorder = order)
	#If this is an "update" of an order, delete old order:
	if len(previouspersonalorder) > 0:
		previouspersonalorder[0].delete()
	#Create a new personal order for this person:
	p1 = PersonalOrder(mealorder = order, user = user, comment = comment, totalcost = totalprice)
	p1.save()
	for item,num in personalorderitems.items():
		mi = MultipleItems.objects.create(personalorder = p1, item = item, num_items = num)
		mi.save()
	p1.save()
	#Return response
	message = "%s just entered an order with total cost $%0.2f at %s." %(user.username, totalprice, timezone.now())
	return render_to_response('enteredorder.html', {'mealorder' : order, 'message' : message, 'personalorder' : p1, 
		"poitems" : personalorderitems}, context_instance=RequestContext(request))
































