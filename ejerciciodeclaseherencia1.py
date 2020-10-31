#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:18:11 2020

@author: daniel
"""

'''
Herencia implicita:
Se define el metodo en la clase madre pero NO en la hija'
'''
class Parent1():
    def implicit(self):
        print("method of the parent")
    def jugarfutbol(self):
        print("Tengo habilidades para el futbol")
    def habilidadesmatematicas(self):
        print("Tengo habilidades matematicas")

class Parent2(Parent1):
    def implicit2(self):
        print("method of the parent")
    def jugarbasketball(self):
        print("Tengo habilidades para el basketball")
    def habilidadeslinguisticas(self):
        print("Tengo habilidades linguisticas")

class Child(Parent2):
    def whoami(self):
        print("I am the child")
#    def implicit(self):
#        print("method of the parent")
    def jugartenis(self):
        print("Tengo habilidades para el tenis")
        
granpa = Parent1()
dad = Parent2()
son = Child()

son.implicit()  #Son may invoke the heritated method
son.jugarfutbol()
son.habilidadesmatematicas()
son.jugartenis()
son.habilidadeslinguisticas()
son.jugarbasketball()




'''
Dada la implementación de la clase Abeja (mostrada abajo), implemente la clase
hija Reina (con los métodos ponerHuevos que imprime Pongo huevos! y emitirFeromonas
que imprime Emito feromonas!)
Finalmente, cree un objeto de tipo Reina y demuestre que la Reina puede acceder 
a objetos heredados de la clase Abeja.

class Abeja :
    def __init__ ( self , sp = " apis mellifera " ) :
        self . especie = sp
    def volar ( self ) :
        print ( " Estoy volando ! " )
    def alimentarse ( self ) :
        print ( " Me estoy alimentando ! " )
'''

