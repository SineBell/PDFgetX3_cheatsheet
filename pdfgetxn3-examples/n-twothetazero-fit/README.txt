Example fit of constant-wavelength neutron PDF nickel data involving
refinement of diffractometer zero which affects PDF conversion.


## Prerequisites

1. Linux or Mac OS X operating system with Anaconda Python

2. Anaconda Environment `nbcmi` with `diffpy-cmi` and `diffpy.pdfgetx`
   installed:

   $ conda create -n nbcmi -c diffpy python=2 diffpy-cmi
   $ conda activate nbcmi
   $ pip install /path/to/diffpy.pdfgetx-VERSION.whl


## Example

Open Jupyter notebook and then run all of its cells

    $ jupyter notebook fit-twothetazero.ipynb
