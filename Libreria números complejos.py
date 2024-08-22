"""Suma
Producto
Resta
División
Módulo
Conjugado
Conversión entre representaciones polar y cartesiano, en los dos sentidos.
Retornar la fase de un número complejo."""

import math

def sum(m,n):

    pReal = m[0] + n[0]
    pImg = m[1] + n[1]
    return pReal, pImg

def product(m,n):

    pReal = (m[0]*n[0])-(m[1]*n[1])
    pImg = (m[0]*n[1])+(n[0]*m[1])
    return pReal, pImg

def subtraction(m,n):

    pReal = m[0] - n[0]
    pImg = m[1] - n[1]
    return pReal, pImg

def division(m,n):
    
    pReal = ((m[0]*n[0]) + (m[1]*n[1])) / ((n[0])**2 + (n[1])**2)
    pImg = ((n[0]*m[1]) - (m[0]*n[1])) / ((n[0])**2 + (n[1])**2)
    return pReal, pImg

def conju(m):
    
    conjuR = m[0]
    conjuI = -1*m[1]
    return conjuR, conjuI

def mod(m):

    modu = (((-3)**2)+(5)**2)**(1/2)
    return modu

def polCar(m):

    carR = m[0] * math.cos(m[1])
    carI = m[0] * math.sin(m[1])
    return carR, carI

def carPol(m):

    polR = mod(m)
    polA = math.atan(m[1]/m[0])
    theta = math.pi -polA
    return polR, theta

def fas(m):

    f = math.atan(m[1]/m[0])
    print("fase: ",f)

def main():

    addends1, addends2 = sum([-3,-5],[7,-9])
    print("suma: ",addends1, addends2)
    multiplying, multiplier = product([-3,-5],[7,-9])
    print("multiplicación: ",multiplying, multiplier)
    minuend, subtracting = subtraction([-3,-5],[7,-9])
    print("resta: ",minuend, subtracting)
    dividend, divider = division([-3,-5],[7,-9])
    print("división: ",dividend, divider)
    conjR, conjI= conju([-3,-5])
    print("conjugado: ",conjR,"+", conjI, "i")
    module = mod([-3,-5])
    print("modulo: ",module)
    cartR, cartI = polCar((-3, 5))
    print("polares a cartesianas: ",cartR, cartI,"i")
    rad, ang = carPol([-3, -5])
    print("cartesianas a polares: ",rad,ang)
    fase = fas([-3,-5])

main()