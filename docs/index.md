
The aim of this documentation is to guide the creation of ligand parameterizations and protein-ligand complex models for use in ufBAC.


## Requirements:

In order to run the full workflow you will need access to two software packages:

1. [AmberTools](http://ambermd.org/#AmberTools) (tested using version 14)
2. [Gaussian](http://gaussian.com/) (tested using Gaussian 09)

AmberTools is free and provided under a GPL license, Gaussian is commercial software.
If Gaussian is not available to you, it is possible to use the semi-empirical AM1-BCC methodology.

Atomic coordinates of the protein-ligand complex are also required (solvent molecules can also be accomodated).
Furthermore, the following restrictions apply to these inputs:

*  coordinates ust be in PDB format 
*  ligand must be located in a suitable initial binding pose
*  protein sequence must be complete with no gaps between residues
*  protein chains must be separated by TER cards



