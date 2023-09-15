This example demonstrates extraction of a PDF from small-angle scattering data.
In this folder, you will find ``Au_DNA_NPA.chi`` and ``Au_DNA_FF.chi`` files which correspond to diffraction data from
DNA-capped Au nanoparticle assemblies and from a DNA-capped Au
nanoparticle colloidal solution respectively. Those two files were
measured at X21 beamline, NSLS and published in `D. Nykypanchuk, M. M.
Maye, D. van der Lelie, and O. Gang, Nature 451, 549 (2008).
<https://www.nature.com/articles/nature06560>`_. We thank Prof. Oleg Gang (Columbia University) for sharing this data. The `pdfgets3.cfg` configuration file specifies processing parameters such as `formfactorfile` (required by ``sas`` mode), `qmin`, `qmax`, and `mode`.

To extract the PDF of DNA-capped Au nanoparticle assemblies, execute following command in this folder

    $ pdfgets3 --verbose=info Au_DNA_NPA.chi

This will save two files in the same directory, `Au_DNA_NPA.fq`, `Au_DNA_NPA.gr` for the F(Q) and G(r) functions of the Au nanoparticle assemblies
