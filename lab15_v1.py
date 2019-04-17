#STUDENTS: Jason Pettit, Marcus Gonzalez
#CST205-40_SP19
#Module 7 Lab 15 - Craps and Python Library

import random
import calendar
import time
from datetime import date

##########################################
#CRAPS
##########################################

def die():
#A single die simulation
  return random.randint(1,6)

def roll():
#A simulation of two dies being rolled
  die1 = die()
  die2 = die()
  sum = die1+die2
  print("You rolled a " + str(die1) + " and " + str(die2) + " your total is " + str(sum))
  return sum  
      
def firstRoll():
  sum = roll()
  
  if (sum == 7 or sum == 11):
    print "7 or 11 you WIN!"
    return 0
  elif (sum == 2 or sum == 3 or sum == 12):
    print "2 or 3 or 12 you lose"
  else:
    print "The point is " + str(sum)
    point = sum
    return point

def rollAgain(point):
  point = point
  rollAgain = 1
  
  while rollAgain != 0:
    roll()
    if roll() == point:
      print "that matches the point " + str(point) + " you WIN!"
      break
    elif roll() == 7:
      print "You rolled a 7, you lose."
      rollAgain = 0

def craps():
  point = firstRoll()
  
  if point != 0:
    rollAgain(point)
      
##########################################
#END CRAPS
##########################################
  
def calendar():
  #this isn't working when I import outside the function
  import calendar
  print "Input your birth year and month"
  year = input("Input your birth year: ")
  month = input("Input your birth month: ")
  print(calendar.month(year, month))
  
def daysTo():
  today = date.today()
  print "Input your birthday and month"
  birthday = input("Input day of the month: ")
  month = input("Input birth month: ")
  
  birthday = date(today.year,month,birthday)
  if birthday < today:
    birthday = date(today.year+1,1,9)
  daysToBirthday = abs(birthday - today)
  print daysToBirthday.days

def dayOfMyBirthday():
  import calendar
  print "Find out what the full date for your birthday was"
  year = input("Input birth year: ")
  month = input("Input your birth month: ")
  day = input("Input day of month: ")
  
  writtenDay = calendar.weekday(year,month,day)
  writtenDay = calendar.day_name[writtenDay]
  
  month = calendar.month_name[month]
  
  print str(writtenDay) + " " + str(month) + " " + str(day) + ", " + str(year) 
  
  