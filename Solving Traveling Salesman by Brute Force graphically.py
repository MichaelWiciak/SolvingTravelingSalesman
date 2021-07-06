import itertools
import turtle
import time
import math
import random

class TravelingSalesman(object):
	def __init__(self):
		self.__city = []
		self.__num = 0
		self.__animate = False
		self.__speed = 100 
		self.__wn = turtle.Screen() 
		turtle.setworldcoordinates(0, 0, 1000, 1000)
		self.__wn.title("TRAVELLING SALESMAN")
		self.__cityPen = turtle.Turtle() 
		self.__cityPen.shape("circle")
		self.__cityPen.hideturtle()
		self.__routePen = turtle.Turtle() 
		self.__routePen.pensize(5) 
		self.__route = [] 
		self.__bestRoute = None 
		self.__bestLength = 1000000 
	
	def main(self):
		self.__title()
		self.__setup()
		self.__generate()
		self.__showCities()
		try:
			self.__getRoutes()
			t0 = time.perf_counter()
			for i in self.__route:
				thisLength = self.__calculateLength(i)
				if thisLength <= self.__bestLength:
					self.__bestLength = thisLength
					self.__bestRoute = i
				if self.__animate:
					self.__showRoute(i)
					time.sleep(0.01)
					self.__routePen.clear()
			print("\nDone. Showing best route")
			print(time.perf_counter() - t0, "seconds")
			self.__showRoute(self.__bestRoute, "green")
			input()
			self.__cityPen.clear()
			self.__routePen.clear()
			self.__routePen.hideturtle()
			self.__cityPen.hideturtle()

		except Exception:
			print("Too many cities.")
				
	def __setup(self):

		ok = False
		while not(ok):
			try:
				num = int(input("Enter number of cities: "))
				if num>1 and num < 11:
					self.__num = num
					ok = True
				else:
					print("Invalid.")
			except Exception:
				pass
		choice = input("Show animation for all? (Y/N): ")
		if choice.lower() in "yes":
			self.__animate = True
			ok = False
			while not(ok):
				try:
					speed = int(input("Select speed (1-10): "))
					if speed >= 0 and speed <= 10:
						self.__speed = speed ** 2
						ok = True
					else:
						print("Invalid.")
				except Exception:
					pass

	def __generate(self):
		for i in range(self.__num):
			x = random.randint(0,1000)
			y = random.randint(0,1000)
			self.__city.append((x,y))
	
	def __showCities(self):
		self.__cityPen.speed(0)
		self.__cityPen.penup()
		for i in range(self.__num):
			self.__cityPen.goto(self.__city[i][0],self.__city[i][1])
			self.__cityPen.stamp()
	
	def __getRoutes(self):
		trylist = list(itertools.permutations(self.__city))
		for i in trylist:
			if i[0] == trylist[0][0]:
				self.__route.append(i)
	
	def __showRoute(self, this, color="red"):
		self.__routePen.color(color)
		self.__routePen.speed(self.__speed)
		self.__routePen.penup()
		for i in this:
			self.__routePen.goto(i[0],i[1])
			self.__routePen.pendown()
		self.__routePen.goto(this[0][0],this[0][1])
			
	def __calculateLength(self, this):
		d = 0
		for i in range(1,len(this)):
			d += math.sqrt( (this[i][0]-this[i-1][0])**2 + (this[i][1]-this[i-1][1])**2)
		return d			
	
	def __title(self):
		print("Solving Traveling Salesman Problem by Brute Force.")

while True:
	app = TravelingSalesman()
	app.main()
