"""
Cálculo do ângulo de contato.
"""

import math

acp = 51
acd = 21.8
aet = 72.8
de = 50.8
aa = float(input('informe o ângulo de contato para a água: '))
ad = float(input('informe o ângulo de contato para o diiodometano: '))

# conversão para radianos
aa = math.radians(aa)
ad = math.radians(ad)

# cálculo da componente dispersiva do sólido cds
cds = (de*(1+math.cos(ad))**2)/4

# cálculo da componente polar do sólido cps
acp = acp**0.5
acd = acd**0.5
cds = cds**0.5
cps = (((aet*(1+math.cos(aa)))/(2*acp))-((acd*cds)/(acp)))**2
cds = cds**2
ess = cds + cps

# output
print('a componente dispersiva do sólido vale: {:.2f} mJ/m2'.format(cds))
print('a componente polar do sólido vale: {:.2f} mJ/m2'.format(cps))
print('a energia de superfície vale: {:.2f} mJ/m2'.format(ess))
