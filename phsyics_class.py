"""
You are a physics teacher preparing for the upcoming semester. 
You want to provide your students with some functions that will help them calculate some 
fundamental physical properties.


Write a function called f_to_c that takes an input f_temp, 
a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.


Write a function called c_to_f that takes an input c_temp, 
a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.

Define a function called get_force that takes in mass and acceleration. 
It should return mass multiplied by acceleration.

Define a function called get_energy that takes in mass and c.

c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. 
Set c to have a default value of 3*10**8.

get_energy should return mass multiplied by c squared.

Define a final function called get_work that takes in mass, acceleration, and distance.

Work is defined as force multiplied by distance. 
First, get the force using get_force, then multiply that by distance. 

"""

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

print(c0_in_fahrenheit)

def get_force(mass,acceleration):
  return mass * acceleration

train_force = (get_force(train_mass, train_acceleration))

print("The GE train supplies " + str(train_force) + " Newtons of force.")

c = 3*10**8

def get_energy(mass, c):
  return mass * c**2

bomb_energy = get_energy(bomb_mass, c)
print(bomb_energy)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

def get_work(mass, acceleration, distance):
  force = get_force(mass,acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print ("The GE train does " + str(train_work) + "Joules of work over " + str(train_distance) + " meters")


