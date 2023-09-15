This example shows how to perform multiple background subtractions when
producing a PDF.

Currently, the only way this can be done is by defining the values of the
configuration parameters "backgroundfile(s)" and "bgscale(s)" within a .cfg file
(refer to "nickel_sub_two_half_backgrounds.cfg" for more details). All other
configuration parameters can be specified on the command line in the usual
manner, as outlined in the rest of the documentation/examples.

To complete this example, refer to the two use cases below:


################################ PDF Production ################################

To simply produce and plot a PDF, first execute

    $ pdfgetx3 -c nickel_sub_two_half_backgrounds.cfg ni300mesh_300k_nor_1-5.chi

This will produce files `ni300mesh_300k_nor_1-5.gr` for G(r) function which can
then be plotted/compared with the expected results (obtained via a single
background subtraction) by executing:

    $ plotdata ni300mesh_300k_nor_1-5-expected.gr ni300mesh_300k_nor_1-5.gr


########################## Interactive PDF Production ##########################

Alternatively, if you wish to produce a PDF and obtain an interactive
environment in which variables related to the PDF production can be queried and
a set of post-production functions can be executed, run the original pdfgetx3
command with the addition of a flag "--plot" (run "$ pdfgetx3 --help" to see
possible options). For example:

    $ pdfgetx3 --force=once --plot=iq,sq,fq,gr \
               -c nickel_sub_two_half_backgrounds.cfg ni300mesh_300k_nor_1-5.chi

Note the inclusion of the flag "--force=(yes|once)" informing pdfgetx3 to
overwrite any previously produced .gr file.

After executing the preceding command, note that in addition to producing a
window displaying the plots, the terminal/command prompt in which you entered
the command will have started a Python session and produced some reference
information listing the variables that can be queried and post-processing
functions that can be executed.

The variables can be queried by simply entering the name provided
as you would any other Python variable, for example:

    In [1]: gr
    Out[1]:
    array([[ 0.00000000e+00,  1.00000000e-02,  2.00000000e-02, ...,
             2.99800000e+01,  2.99900000e+01,  3.00000000e+01],
           [ 0.00000000e+00, -2.72254807e-03, -5.26172439e-03, ...,
             4.92635507e-01,  5.45568967e-01,  5.96090017e-01]])

Similarly, the functions listed can be executed as any other Python function.
For example, to bring up a window that provides a graphical user interface (GUI)
allowing you to manipulate the configuration parameters (e.g. bgscale(s), qmin,
qmax, etc.), execute:

    In [2]: tuneconfig()

Which should produce a new window containing a set of controls (e.g., sliders)
that can be manipulated to modify the plotting parameters and their effect is
immediately reflected in the plots.
