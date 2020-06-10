#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

m, x, y, z = np.loadtxt('halo.txt', usecols=(0,1,2,3), unpack=True)

density = []
radii = []

Nshells = 50       #número de cascas esféricas
rmax = 50          #até onde calcular a densidade de matéria escura
dr = rmax/Nshells   #diferença de raio entre cada casca

#Pitágoras, pois precisaremos da distância absoluta de cada partícula ao centro
r = np.sqrt(x**2 + y**2 + z**2)

for i in range(Nshells):
  r1 = i * dr
  r2 = r1 + dr

  #definindo shell como a lista de partículas que estão dentro da casca
  shell = np.argwhere( (r > r1) & (r < r2) ).flatten()

  mass = sum(m[shell])
  volume = 4/3.0 * np.pi * (r2**3 - r1**3)
  rho = mass/volume

  radius = (r1 + r2)/2.0

  density.append(rho)
  radii.append(radius)

plt.plot(radii, density, c='red')
plt.xlabel('r (kpc)')
plt.ylabel('$\\rho$ ($M_{\\odot}/kpc^3$)')
plt.yscale('log')
plt.show()
plt.close()
