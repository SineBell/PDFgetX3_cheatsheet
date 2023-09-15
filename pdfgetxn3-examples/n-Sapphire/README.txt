This example shows PDF extraction from neutron powder data using `pdfgetn3`.
The `sapphire755.dat` file contains powder diffraction data from sapphire
(alpha-Al2O3) measured at the constant-wavelength PEARL instrument
at the Delft University of Technology.
The `pdfgetn3.cfg` configuration file specifies processing parameters such as
wavelength, twothetazero, chemical composition, and neutron processing mode.

To extract the sapphire neutron PDF execute

    $ pdfgetn3 --verbose=info sapphire755.dat

This will produce two files `sapphire755.fq`, `sapphire755.gr`
for the F(Q) and G(r) functions.  To compare them with expected results use

    $ plotdata sapphire755-expected.fq sapphire755.fq
    $ plotdata sapphire755-expected.gr sapphire755.gr
