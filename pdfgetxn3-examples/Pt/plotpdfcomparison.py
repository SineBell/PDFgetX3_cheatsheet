#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from diffpy.pdfgetx import loaddata

r0, g0 = loaddata('Pt_bulk-00055-pdfgetx2.gr', usecols=(0, 1)).T
r1, g1 = loaddata('Pt_bulk-00055-pdfgetx3.gr', usecols=(0, 1)).T
g1s = max(g0) / max(g1) * g1
gds = g0 - np.interp(r0, r1, g1s)

fig, ax = plt.subplots()
ax.plot(r0, g0, label='PDFGetX2, Qmax=27/A')
ax.plot(r1, g1s, label='PDFGetX3, Qmax=27/A, scaled')
ax.plot(r0, gds - 10, label='difference curve')
ax.legend(fontsize='small')
ax.set_title('Pt')
ax.set_xlabel('r (A)')
ax.set_ylabel('G (A$^{-2}$)')
plt.show()
