# -*- coding: utf-8 -*-
"""derivative_and_hessian.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10dOJpbECBSsB4Jr0jN6bsaVbDuf1qEAO
"""

import sympy

def funcao(x): # x^2 + y^2
  return x[0]**2 + x[1]**2

nro_variaveis = 2

variaveis = sympy.symbols('x0:%d'%nro_variaveis)

print(" Gradientes: ")
grad = []
for j in range(nro_variaveis):
  diff = sympy.diff(funcao(variaveis), variaveis[j])
  grad.append(diff)
  print(diff)

print(" Hessiana")
for g in range(nro_variaveis):
  for j in range(nro_variaveis):
    print(sympy.diff(grad[g], variaveis[j]), end=', ')
  print()