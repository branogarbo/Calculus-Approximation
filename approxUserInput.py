from random import *
from math import *

samp = 999999
h = 1/samp

# Utility fuctions

def uArs(f,a,b):
  dx = (b-a)/samp
  s = 0

  for i in range(samp):
    s += f(a+i*dx)*dx

  return s

udiff = lambda f,p: (f(p+h)-f(p))/h
usecDiff = lambda f,p: (udiff(f,p+h)-udiff(f,p))/h

partialDiffX = lambda f,x,y: (f(x+h,y)-f(x,y))/h
partialDiffY = lambda f,x,y: (f(x,y+h)-f(x,y))/h

############################################################

# Monte-Carlo Integration (F : R → R)

def Amc(f,a,b):
  tot,tru = 0,0
  up = f(a)+f(b)
  rec = (b-a)*up

  for i in range(samp):
    tot += 1
    if uniform(0,up) < f(uniform(a,b)):
      tru += 1
  area = tru/tot*rec

  print("A =",area)

# Derivative (F : R → R)

def diff(f,p):
  print("f'("+str(p)+") =",udiff(f,p))

# Riemann Sum (F : R → R)

def Ars(f,a,b):
  print("A =",uArs(f,a,b))

# Curvature (F : R → R)

def curv(f,p):
  c = usecDiff(f,p)/(1+udiff(f,p)**2)**(3/2)

  print("K("+str(p)+") =",c)

# Curvature (F : R → R2)

def curvPara(f,g,t):
  c = (udiff(f,t)*usecDiff(g,t)-udiff(g,t)*usecDiff(f,t))/(udiff(f,t)**2+udiff(g,t)**2)**(3/2)

  print("K("+str(t)+") =",c)

# Line Integral (F : R → R2, q : R2 → R)

def lineInt(f,g,q,a,b):
  u = uArs(lambda t: q(f(t),g(t))*(udiff(f,t)**2+udiff(g,t)**2)**(1/2),a,b)

  print("A =",u)

eval(input("Enter function to execute: "))