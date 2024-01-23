import pizza

pizza.make_pizza(40, 'peperoni')
pizza.make_pizza(30, 'tomato', 'onions', 'olives')

#I am creating pizza with the size of 40 cm with the following ingredients:
#-peperoni

#I am creating pizza with the size of 30 cm with the following ingredients:
#-tomato
#-onions
#-olives

from pizza import make_pizza as mp #if there is a need we can change the name of the funtion

mp(40, 'peperioni')
mp(30, 'tomato', 'onions', 'olives')

