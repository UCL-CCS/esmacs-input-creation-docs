# BAC ESMACS Input Creation

The aim of this documentation is to guide the creation of ligand parameterizations and protein-ligand complex models for use in ufBAC.
It only covers the single ligand parameterization required for the ESMACS family of protocols.

## Requirements

In order to run the full workflow you will need access to two software packages:

1. [AmberTools](http://ambermd.org/#AmberTools) (tested using version 14)
2. [Gaussian](http://gaussian.com/) (tested using Gaussian 09)

AmberTools is free and provided under a GPL license, Gaussian is commercial software.
If Gaussian is not available to you, it is possible to use the semi-empirical AM1-BCC methodology.

Atomic coordinates of the protein-ligand complex are also required (solvent molecules can also be accommodated).
Furthermore, the following restrictions apply to these inputs:

*  coordinates must be in PDB format
*  all protein residues **must** be available in the standard Amber forcefield
*  ligand must be located in a suitable initial binding pose
*  protein sequence must be complete with no gaps between residues

It is assumed throughout that the reader is familiar with the PDB format used to store atomic coordinates.
We further suppose that you either have the AmberTools available in your run path or know how to adapt the path used to execute the commands.

## Outcomes

This tutorial will run through all the steps needed to prepare protein-ligand system for ESMACS.
It details the calculation of appropriate partial charges via Gaussian and the Antechamber tool and production of Amber *prep* and *frcmod* files containing the ligand parameterization.
Additionally, it details the modified PDB format required by BAC and how to verify your model is suitable for simulation.
Instructions are then provided on combining the PDB and forcefield files ready for upload to ufBAC.
