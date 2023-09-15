#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from diffpy.pdfgetx import loaddata

r0, g0 = loaddata('si90ni10_300k_nor_1-6-pdfgetx2.gr', usecols=(0, 1)).T
r1, g1 = loaddata('si90ni10_300k_nor_1-6-pdfgetx3.gr', usecols=(0, 1)).T
g1s = max(g0) / max(g1) * g1
gds = g0 - np.interp(r0, r1, g1s)

fig, ax = plt.subplots()
ax.plot(r0, g0, label='PDFGetX2, Qmax=27/A')
ax.plot(r1, g1s, label='PDFGetX3, Qmax=26/A, scaled')
ax.plot(r0, gds - 4, label='difference curve')
ax.legend(fontsize='small')
ax.set_title('weight mixture Si0.9-Ni0.1')
ax.set_xlabel('r (A)')
ax.set_ylabel('G (A$^{-2}$)')
ax.set_xlim(0, 30)
plt.show()
