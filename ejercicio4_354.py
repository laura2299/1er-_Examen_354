# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:24:41 2023

@author: WINDOWS 11
"""

from kanren import Relation, facts,var,run,lall
from kanren.constraints import neq

x=var()
parentera=Relation()
facts(parentera,("Eliseo","Laura"),
            ("Eliseo","Cesar"),
            ("Eliseo","Naira"),
            ("Eliseo","Alan"),
            ("Martin","Eliseo"),
            ("Martin","Rosa"),
            ("Martin","Daniel"),
            ("Rosa","Celina"),
            ("Rosa","Yesica"),
            ("Daniel","Riana")
            )


def hijos(x,y):
  return lall(parentera(y,x))

def abuelos(x,z):
  y=var()
  return lall(parentera(x,y),parentera(y,z))
def hermanos(x,y):
  p=var()
  return lall(parentera(p,y),hijos(x,p),neq(x,y))
def tios(x1,z):
  y=var()
  x2=var()
  return lall(parentera(x2,z),hermanos(x1,x2))
def primos(x,y):
  p1=var()
  p2=var()
  return lall(parentera(p2,y),hermanos(p1,p2),hijos(x,p1))

print("Abuelos de Alan:")
print(run(4,x,abuelos(x,"Alan")))
print("Hermans de Cesar:")

print(run(5,x,hermanos(x,"Cesar")))
print("Hijos de Eliseo:")

print(run(4,x,hijos(x,"Eliseo")))
print("Tios de Celina:")

print(run(4,x,tios(x,"Celina")))
print("Primos de Celina:")

print(run(10,x,primos(x,"Celina")))


