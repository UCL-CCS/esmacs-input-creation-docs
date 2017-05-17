
The next stage will require that any hydrogens which are part of the ligand are added (these are usually not resolved in crystal structures).
AmberTools provides a tool for estimating the protonation of ligands called reduce.
To use this tool on the example 4BJX ligand extracted in the last section use the command:

```
reduce 4bjx-ligand.pdb > 4bjx-ligand-h.pdb
```

A wide variety of other ways to add these atoms are possible, one popular option is [OpenBabel](http://openbabel.org/).

## Initial steps using Antechamber

Antechamber is designed to allow the rapid generation of topology files for ligands using the generalized Amber force field (GAFF).
Two charge methods can be used HF/6-31G RESP\* or AM1-BCC.
The work conducted to date with BAC has focussed on the HF/6-31G\* RESP method used to parameterize much of the main Amber forcefield.
It is this approach that we will be detailing in the next two sections, although we will briefly mention the command used to complete the AM1-BCC approach as this eliminated the need for time consuming Gaussian calculations.

The first step to using Antechamber in this context is to generate the input file for Gaussian to optimize the ligand and generate a quantum-chemically calculated electrostatic potential.

For neutral ligands it is sufficient to specify only the input PDB (`-fi` specifies the format and `-i` the filename) and the output file (`-fo` specifies the format and `-o` the filename):

```
antechamber -fi pdb -fo gcrt -i 4bjx-ligand-h.pdb -o 4bjx-ligand.gau
```

If the ligand is charged and extra option for the net charge, `-nc`, must be used.
For example if we thought the ligand had a charge of +1 we would use:

```
antechamber -fi pdb -fo gcrt -i 4bjx-ligand-h.pdb -o 4bjx-ligand.gau -nc 1
```

The first few lines of the Gaussian input file generated will look something like this:

```
--Link1--
%chk=molecule
#HF/6-31G* SCF=tight Test Pop=MK iop(6/33=2) iop(6/42=6) opt

remark line goes here

0   1
    C   15.0320000000        6.0240000000       10.0040000000     
    C   14.0090000000        5.1520000000        9.2570000000     
    C   14.6530000000        4.2700000000        8.1860000000
```

The meaning of the Gaussian options, found in the third line, are as follows:

* Opt: We ask for optimization of our structure
* HF/6-31G\*: We are using the 6-31G\* basis set
* Pop=MK: The output will contain Merz-Kollman atomic charges (fitted to the electrostatic potential)
* iop(6/33=2): Output grid of values of describing the electrostatic potentail.
This will used in the latter RESP step to create the partial charges used in the final parameterization.

The values on line 7 are the net charge and the multiplicity.

### Non-standard approach (using AM1-BCC)

This section is something of an aside and is included for completeness only, skip if you are only interested in creating standard BAC parameterizations.
If you wish to create the topology without Gaussian optimization and using the AM1-BCC approach to charges this can be achieved with a single command:

```
antechamber -i 4bjx-ligand-h.pdb -fi pdb -o l01.prep -fo prepi -c bcc -at gaff -j 4 -rn L01
```

Here the ligand is renamed 'L01'.

If you use this approach you can skip the section below on Gaussian and the next Antechamber step and move straight to the [BAC input generation]() section.

## Geometry optimization (Gaussian)

To run the geometry optimization in Gaussian and obtain the electrostatic potential it is a simple Gaussian run.
In principle this can be achieved using the command (for Gaussian 09):

```
g09 < 4bjx-ligand.gau > 4bjx-ligand.out
```

However, this process can take a long time and it is recommended that the job is executed using a batch system. The details of executing that run will be dependent on your system setup.

In the next section we will use the electrostatic potential to generate partial charges for our ligand.
