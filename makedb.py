from lunch2.models import Restaurant, Item, ItemType
from django.utils import timezone

r1 = Restaurant(name = "Dos Toros", address = "137 4th Avenue, New York, NY 212-677-7300", 
	website = "http://dostoros.com")
r1.save()

t0101 = r1.itemtype_set.create(name="Burrito", 
	description="Includes Rice, Black or Pinto Beans, Cheese, Salsa, and Sour Cream.")
t0102 = r1.itemtype_set.create(name="Taco",
	description="Includes Cheese, Salsa, and Sour Cream.")
t0103 = r1.itemtype_set.create(name="Quesadilla", 
	description="Includes Cheese, Salsa, and Sour Cream.")
t0104 = r1.itemtype_set.create(name="Plato or Salad", 
	description="Same as a burrito, minus the tortilla. The Salad is just like the Plato, on a bed of lettuce.")
t0105 = r1.itemtype_set.create(name="Sides", description="")
t0106 = r1.itemtype_set.create(name="Drinks", description="")

t0101.save()
t0102.save()
t0103.save()
t0104.save()
t0105.save()
t0106.save()

i0101 = t0101.item_set.create(restaurant_id = r1.id, name="Carnitas (braised pork)", price=8.04)
i0102 = t0101.item_set.create(restaurant_id = r1.id, name="Pollo Asado (grilled chicken)", price=8.04)
i0103 = t0101.item_set.create(restaurant_id = r1.id, name="Carne Asada (grilled steak)", price=8.50)
i0104 = t0101.item_set.create(restaurant_id = r1.id, name="Basic (rice and beans)", price=6.67)
i0105 = t0101.item_set.create(restaurant_id = r1.id, name="Add guacamole", price=0.92)

i0106 = t0102.item_set.create(restaurant_id = r1.id, name="Carnitas (braised pork)", price=3.90)
i0107 = t0102.item_set.create(restaurant_id = r1.id, name="Pollo Asado (grilled chicken)", price=3.90)
i0108 = t0102.item_set.create(restaurant_id = r1.id, name="Carne Asada (grilled steak)", price=4.13)
i0109 = t0102.item_set.create(restaurant_id = r1.id, name="Basic (rice and beans)", price=3.28)
i0110 = t0102.item_set.create(restaurant_id = r1.id, name="Add guacamole", price=0.46)

i0111 = t0103.item_set.create(restaurant_id = r1.id, name="Carnitas (braised pork)", price=6.67)
i0112 = t0103.item_set.create(restaurant_id = r1.id, name="Pollo Asado (grilled chicken)", price=6.67)
i0113 = t0103.item_set.create(restaurant_id = r1.id, name="Carne Asada (grilled steak)", price=7.12)
i0114 = t0103.item_set.create(restaurant_id = r1.id, name="Basic (rice and beans)", price=5.51)
i0115 = t0103.item_set.create(restaurant_id = r1.id, name="Cheese", price=3.67)
i0116 = t0103.item_set.create(restaurant_id = r1.id, name="Add guacamole", price=0.92)

i0117 = t0104.item_set.create(restaurant_id = r1.id, name="Carnitas (braised pork)", price=8.04)
i0118 = t0104.item_set.create(restaurant_id = r1.id, name="Pollo Asado (grilled chicken)", price=8.04)
i0119 = t0104.item_set.create(restaurant_id = r1.id, name="Carne Asada (grilled steak)", price=8.50)
i0120 = t0104.item_set.create(restaurant_id = r1.id, name="Basic (rice and beans)", price=6.67)
i0121 = t0104.item_set.create(restaurant_id = r1.id, name="Add guacamole", price=0.92)

i0122 = t0105.item_set.create(restaurant_id = r1.id, name="Chips", price=0.92)
i0123 = t0105.item_set.create(restaurant_id = r1.id, name="Chips and Salsa", price=2.07)
i0124 = t0105.item_set.create(restaurant_id = r1.id, name="Chips and Guacamole", price=3.22)
i0125 = t0105.item_set.create(restaurant_id = r1.id, name="Guacamole", price=2.53)
i0126 = t0105.item_set.create(restaurant_id = r1.id, name="Salsa", price=1.38)

i0127 = t0106.item_set.create(restaurant_id = r1.id, name="Soda", price=1.61)
i0128 = t0106.item_set.create(restaurant_id = r1.id, name="Bottled Water", price=1.84)
i0129 = t0106.item_set.create(restaurant_id = r1.id, name="Bottle Drinks", price=2.53)
i0130 = t0106.item_set.create(restaurant_id = r1.id, name="Tecate", price=2.76)
i0131 = t0106.item_set.create(restaurant_id = r1.id, name="Corona, Pacifico, Negra Modelo", price=4.13)

i0101.save()
i0102.save()
i0103.save()
i0104.save()
i0105.save()
i0106.save()
i0107.save()
i0108.save()
i0109.save()
i0110.save()
i0111.save()
i0112.save()
i0113.save()
i0114.save()
i0115.save()
i0116.save()
i0117.save()
i0118.save()
i0119.save()
i0120.save()
i0121.save()
i0122.save()
i0123.save()
i0124.save()
i0125.save()
i0126.save()
i0127.save()
i0128.save()
i0129.save()
i0130.save()
i0131.save()

r2 = Restaurant(name = "Hill Country Chicken", address = "1123 Broadway (Corner of 25th) New York, NY 10010 212-257-6446", 
	website = "http://www.hillcountrychicken.com/")
r2.save()

t0201 = r2.itemtype_set.create(name="Pies", 
	description="Assumes 1 medium pie. Add comment if you want a different size.")
t0202 = r2.itemtype_set.create(name="Fried Chicken - Hill Country Classic",
	description="Classic southern fried chicken: seasoned with our signature shake.")
t0203 = r2.itemtype_set.create(name="Fried Chicken - Mama El's Recipe", 
	description="Our special family recipe: skinless with a crunchy, cracker crust.")
t0204 = r2.itemtype_set.create(name="Texas Tenders", 
	description="Assumes 3 pieces, comment if you would like a larger size (5 pc $12, 10pc $23).")
t0205 = r2.itemtype_set.create(name="Sandwiches and Salads", description="")
t0206 = r2.itemtype_set.create(name="Sides", description="")
t0207 = r2.itemtype_set.create(name="Beverages", description="")
t0208 = r2.itemtype_set.create(name="Premium Ice Cream and Shakes", description="")

t0201.save()
t0202.save()
t0203.save()
t0204.save()
t0205.save()
t0206.save()
t0207.save()
t0208.save()

i0201 = t0201.item_set.create(restaurant_id = r2.id, name="Apple Cheddar", price=6.50)
i0202 = t0201.item_set.create(restaurant_id = r2.id, name="Double Cherry", price=6.50)
i0203 = t0201.item_set.create(restaurant_id = r2.id, name="Banana Cream", price=6.50)
i0204 = t0201.item_set.create(restaurant_id = r2.id, name="Bourbon Pecan", price=6.50)
i0205 = t0201.item_set.create(restaurant_id = r2.id, name="Cowboy", price=6.50)
i0206 = t0201.item_set.create(restaurant_id = r2.id, name="Texas Billionaire", price=6.50)
i0207 = t0201.item_set.create(restaurant_id = r2.id, name="Coconut Cream", price=6.00)
i0208 = t0201.item_set.create(restaurant_id = r2.id, name="Creme Brulee", price=6.00)
i0209 = t0201.item_set.create(restaurant_id = r2.id, name="Salted Margarita", price=6.00)
i0210 = t0201.item_set.create(restaurant_id = r2.id, name="Pig Pickin'", price=6.00)
i0211 = t0201.item_set.create(restaurant_id = r2.id, name="Whiskey Buttermilk", price=6.00)
i0212 = t0201.item_set.create(restaurant_id = r2.id, name="Lemon Meringue", price=6.00)

i0213 = t0202.item_set.create(restaurant_id = r2.id, name="Breast", price=5.50)
i0214 = t0202.item_set.create(restaurant_id = r2.id, name="Thigh", price=3.50)
i0215 = t0202.item_set.create(restaurant_id = r2.id, name="Drum", price=2.25)
i0216 = t0202.item_set.create(restaurant_id = r2.id, name="Wing", price=1.75)
i0217 = t0202.item_set.create(restaurant_id = r2.id, name="Pick of the Chick", price=27.00)

i0218 = t0203.item_set.create(restaurant_id = r2.id, name="Breast", price=5.50)
i0219 = t0203.item_set.create(restaurant_id = r2.id, name="Thigh", price=3.50)
i0220 = t0203.item_set.create(restaurant_id = r2.id, name="Drum", price=2.25)
i0221 = t0203.item_set.create(restaurant_id = r2.id, name="Wing", price=1.75)
i0222 = t0203.item_set.create(restaurant_id = r2.id, name="Pick of the Chick", price=27.00)

i0223 = t0204.item_set.create(restaurant_id = r2.id, name="Buttermilk Ranch", price=7.50)
i0223 = t0204.item_set.create(restaurant_id = r2.id, name="Hill Country Barbecue", price=7.50)
i0223 = t0204.item_set.create(restaurant_id = r2.id, name="Honey Mustard", price=7.50)

i0224 = t0205.item_set.create(restaurant_id = r2.id, name="Texas Hand Roll", price=5.00)
i0225 = t0205.item_set.create(restaurant_id = r2.id, name="2 Texas Hand Rolls", price=9.00)
i0226 = t0205.item_set.create(restaurant_id = r2.id, name="Chickwich", price=8.00)
i0227 = t0205.item_set.create(restaurant_id = r2.id, name="Mama Els' Salad", price=10.25)
i0228 = t0205.item_set.create(restaurant_id = r2.id, name="Mama Els' Salad - No Chicken", price=6.50)
i0229 = t0205.item_set.create(restaurant_id = r2.id, name="Mama Els' Salad - No Chicken, Small", price=3.00)
i0230 = t0205.item_set.create(restaurant_id = r2.id, name="Hill Country Club", price=10.00)
i0231 = t0205.item_set.create(restaurant_id = r2.id, name="Fried Pimiento Cheese Sandwich", price=5.00)
i0232 = t0205.item_set.create(restaurant_id = r2.id, name="Kickin' Chicken Salad", price=9.75)

i0233 = t0206.item_set.create(restaurant_id = r2.id, name="Fresh Cut Fries Small", price=2.50)
i0234 = t0206.item_set.create(restaurant_id = r2.id, name="Fresh Cut Fries Large", price=4.00)
i0235 = t0206.item_set.create(restaurant_id = r2.id, name="Buttermilk Biscuit", price=1.00)
i0236 = t0206.item_set.create(restaurant_id = r2.id, name="Blistered Corn Salad Small", price=2.50)
i0237 = t0206.item_set.create(restaurant_id = r2.id, name="Carrot-n-raisin Slaw", price=2.50)
i0238 = t0206.item_set.create(restaurant_id = r2.id, name="Cheesy Fried Mash Potatoes", price=2.50)
i0239 = t0206.item_set.create(restaurant_id = r2.id, name="Creamy Coleslaw", price=2.50)
i0240 = t0206.item_set.create(restaurant_id = r2.id, name="Pimento Mac and Cheese Small", price=3.00)
i0241 = t0206.item_set.create(restaurant_id = r2.id, name="Pimento Mac and Cheese Large", price=6.00)
i0242 = t0206.item_set.create(restaurant_id = r2.id, name="Chicken Salad Small", price=4.50)
i0243 = t0206.item_set.create(restaurant_id = r2.id, name="Chicken Salad Large", price=8.00)
i0244 = t0206.item_set.create(restaurant_id = r2.id, name="Picnic Stix: Carrots and Celery", price=2.00)

i0245 = t0207.item_set.create(restaurant_id = r2.id, name="Fountain Soda", price=2.50)
i0246 = t0207.item_set.create(restaurant_id = r2.id, name="Boylan's Bottles", price=4.00)
i0247 = t0207.item_set.create(restaurant_id = r2.id, name="Hand Squeezed Lemonade", price=3.25)
i0248 = t0207.item_set.create(restaurant_id = r2.id, name="Poland Spring Bottled Water", price=2.00)
i0249 = t0207.item_set.create(restaurant_id = r2.id, name="Mozart's HC Blend Coffee Small", price=2.00)
i0250 = t0207.item_set.create(restaurant_id = r2.id, name="Mozart's Cold Brew Iced Coffee Small", price=2.00)

i0251 = t0208.item_set.create(restaurant_id = r2.id, name="Milkshake - Vanilla, Black&White, Coffee, and Mocha", price=5.00)
i0252 = t0208.item_set.create(restaurant_id = r2.id, name="Pie Shake - Made with Vanilla ice cream and pie of the day", price=6.00)
i0253 = t0208.item_set.create(restaurant_id = r2.id, name="Ice Cream Float- Made with vanilla ice cream and boylan soda flavors", price=5.00)


i0201.save()
i0202.save()
i0203.save()
i0204.save()
i0205.save()
i0206.save()
i0207.save()
i0208.save()
i0209.save()
i0210.save()
i0211.save()
i0212.save()
i0213.save()
i0214.save()
i0215.save()
i0216.save()
i0217.save()
i0218.save()
i0219.save()
i0220.save()
i0221.save()
i0222.save()
i0223.save()
i0224.save()
i0225.save()
i0226.save()
i0227.save()
i0228.save()
i0229.save()
i0230.save()
i0231.save()
i0232.save()
i0233.save()
i0234.save()
i0235.save()
i0236.save()
i0237.save()
i0238.save()
i0239.save()
i0240.save()
i0241.save()
i0242.save()
i0243.save()
i0244.save()
i0245.save()
i0246.save()
i0247.save()
i0248.save()
i0249.save()
i0250.save()
i0251.save()
i0252.save()
i0253.save()
























