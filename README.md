## DiBaseRNA: Database and Atlas of Nucleobase Spatial Arrangements in RNA ##


### Description of the files and folders ###

DiBaseRNA_DB:

the folder with the actual structure files that comprise the database. 

DiBaseRNA_DB/DiBaseRNA_A:

the database with hydrogen atoms optimised by AM1. Optimisation of only the hydrogen positions are done on each of the dimeric structures, with non-planarities removed by projecting the hydrogens onto the ring plane.

DiBaseRNA_DB/DiBaseRNA_B:

the database where the monomers in each of the dimeric structures are constructed from the etalon A, G, U and C structures obtained by tight RB3LYP/6-311+G(2d,p) optimisation. Thus, only the interring positions are inferred from the experimental RNA structures.

DiBaseRNA_DB/DiBaseRNA_B/DiBaseRNA_metadata.txt:

the file with the structure and source information for each structure file in the database, mapping the information onto the used RNA05 structure database.

DiBaseRNA_ATLAS:
the folder with all the stereo visualisation files and figures for the DiBaseRNA database.

DiBaseRNA_ATLAS/Chimera_scenes:

the folder with the 3D visualisation files to be used with USCF Chimera program.

DiBaseRNA_ATLAS/DiBaseRNA_ATLAS.docx:

the MS Word source of the DiBaseRNA_ATLAS.pdf file.

DiBaseRNA_ATLAS.pdf:

the visual guide to the DiBaseRNA database.


### How to cite the DiBaseRNA database and atlas? ###
Sahakyan A.B. and Vendruscolo M, “DiBaseRNA: Database and Atlas of Nucleobase Spatial Arrangements in RNA”, 2013+. https://github.com/aleksahak/DiBaseRNA
Sahakyan A.B. and Vendruscolo M. “Analysis of Ring Current and Electric Field Effects on the Chemical Shifts of RNA Bases”, J. Phys. Chem. B, 117, 1989-1998, 2013. http://dx.doi.org/10.1021/jp3057306


### How has the DiBaseRNA atlas been constructed? ###

  The initial RNA structures were taken from the RNA05 database of Richardson and co-workers[1], which contained 171 coordinate files of RNA X-ray structures with 9486 nucleotide content and 3.0 Å or better resolution. Then, all the structures with equal to or better than 1.8 Å resolution were scanned, and all the possible dibase arrangements between any pair among the conjugated rings of adenine (A), guanine (G), cytosine (C), and uracil (U) bases were retrieved.

  The dibase geometries were classified into three categories: with adjacent (ADJ), spatial (SPT), and hydrogen bonded (HBD) arrangements.

  In this context, ADJ indicates that, in the XY arrangement of the bases X and Y, the conjugated rings belong to the neighbouring nucleotides within the same chain. The adjacent dibases were scanned in both 5′ to 3′ and 3′ to 5′ directions for the retrieval. In cases where one of the dibase members was common in both directions (for instance, if we search for the adjacent arrangement of GA in the GAG sequence, A will be common in GA moieties retrieved from both directions), the fragment from the 3′ to 5′ scan was discarded.

  HBD refers to the arrangement where the bases are nearly coplanar with hydrogen bonds (either classical Watson-Crick or of other types) between them and can belong to the same or different polynucleotide chains.

  The SPT arrangement is defined as the one where the two bases are not coplanar and belong to either different chains or the same chain but separated by at least 3 nucleotides. They would usually represent the diagonal arrangement of the base-rings for the situations where the RNA molecule is self-assembled into local double helical structures.

  Next, hydrogens were added to the N9 and N1 positions of the purine and pyrimidine rings as a replacement of the glycosidic bond, so that the resulting coordinate files corresponded to a complete and closed-shell system of two bases, ready for quantum chemical calculations.

  The DiBaseRNA database was further refined by a partial geometry optimisation with frozen core atoms via the semiempirical AM1 Hamiltonian[2] as implemented in the MOPAC2009 package[3]. The AM1 was selected, taking into account its accuracy in representing the amide bond lengths[4] and the geometries of amino groups attached to conjugated systems[5]. Furthermore, the known issue of nitrogen pyramidality overestimation is the least pronounced for AM1[4] in NDDO-type (neglect of diatomic differential overlap) semiempirical methods. In order to remove the residual pyramidality, the N−H bonds were further frozen to be within the same plane as the corresponding conjugated ring. The resulting coordinate files in PDB format represent the variant A of the DiBaseRNA database (DiBaseRNA_A) that features experimentally determined positions of the core atoms of each of the conjugated systems.

   However, small structural variations in the experimental bond lengths within the ring, caused by the experimental errors, are inevitable. Hence, another variant of the DiBaseRNA database was generated (variant B, DiBaseRNA_B), where only the relative arrangement of the two rings were learned from the X-ray data and the final files were constructed by rotating and translating the standard (predefined) geometries of the constituent bases to match the experimental arrangement. To obtain the standard geometries, A, G, C, and U bases were geometry optimised without any constraints and with tight convergence criteria. Hybrid density functional theory[6] via the Becke three-parameter exchange functional and the Lee, Yang, and Parr correlation functional (B3LYP)[7-9] was used with the split-valence 6-311+G(2d,p) basis set[10]. After the geometry optimisation, amino groups in adenine, guanine, and cytosine did appear to be slightly out of plane of the conjugated system; however, a certain level of the out-of-plane displacement is not an artefact of the calculation and are observed by both experimental and more sophisticated theoretical methods[11,12].

[1] Murray, L. J. W.; Arendall, W. B.; Richardson, D. C.; Richardson, J. S. Proc. Natl. Acad. Sci. U.S.A. 2003, 100, 13904−13909.
[2] Dewar, M. J. S.; Zoebisch, E. G.; Healy, E. F.; Stewart, J. J. P. J. Am. Chem. Soc. 1985, 107, 3902−3909.
[3] Stewart, J. J. P. MOPAC2009; Stewart Computational Chemistry: Colorado Springs, CO, 2008.
[4] Stewart, J. J. P. J. Mol. Model. 2007, 13, 1173−1213.
[5] Yatsenko, A. V.; Paseshnichenko, K. A. J. Mol. Struct. 1999, 492, 277−283.
[6] Kohn, W.; Sham, L. J. Phys. Rev. A 1965, 140, 1133−1138.
[7] Lee, C.; Yang, W.; Parr, R. G. Phys. Rev. B 1988, 37, 785−789.
[8] Miehlich, B.; Savin, A.; Stoll, H.; Preuss, H. Chem. Phys. Lett. 1989, 157, 200−206.
[9] Becke, A. D. J. Chem. Phys. 1993, 98, 5648−5652.
[10] Krishnan, R.; Binkley, J. S.; Seeger, R.; Pople, J. A. J. Chem. Phys. 1980, 72, 650−654.
[11] Šponer, J.; Hobza, P. J. Phys. Chem. 1994, 98, 3161−3164.
[12] Sychrovsky, V.; Foldynova-Trantirkova, S.; Spackova, N.; Robeyns, K.; Meervelt, L. V.; Blankenfeldt, W.; Vokacova, Z.; Sponer, J.; Trantirek, L. Nucleic Acids Res. 2009, 37, 7321−7331.
