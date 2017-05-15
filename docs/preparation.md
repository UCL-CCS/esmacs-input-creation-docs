
The BAC Builder script requires the input PDB structure to follow a particular format.

1. All chains to be included in the final model must have coordinates present (BIOMT records, etc. will not be applied)
2. The sequence must contain unambiguous coordinates for each residue and atom (i.e. no alternative locations or residues)
3. All hydrogen atoms should be removed
3. Chains must contain no gaps and residues numbered sequentially
4. Each chain must have a unique ID and end with a TER card
5. Chains must be present in a particular order: protein, ligand, solvent.
6. All residues included must be compatible with the Amber forcefield. In the case of the ligand, this means that the included version of the coordinates should be those generated during parameterization (to ensure atom names are consistent).

Models for preparation in BAC can come from many sources but a common scenario is that the starting point is a PDB containing coordinates for all components of the system.
In this section we detail the steps necessary to create a BAC input PDB from such a model.
The PDB [4BJX](examples/4bjx.pdb) is used as an example to illustrate the general process (it can be downloaded from the link for using following along).

In this example we assume that you begin with a PDB containing all elements of the system.
Where multiple ligands are to be added to the same protein receptor then once the protein structure has been prepares once you can skip to the [ligand preparation](#prepare-ligand) section to create input for parameterization.

## Protein model

The example structure contains a protein, ligand and solvent molecules (see picture below).
The first step is to separate the protein chains and ensure they are ready for incorporation in the final model.

![4BJX structure](images/4bjx-init.png)

The protein model must be extracted from the PDB.
Simple ways of achieving this in general include the use of protein selections within viewers such as [VMD](http://www.ks.uiuc.edu/Research/vmd/) or using a text editor.
In the case of the 4BJX the protein residues are the only ones listed using `ATOM` records meaning that a `sed` in Linux command can be used to gain the proein residues alone:




`pdb4amber` which is part of the AmberTools package (use the `--help` flag to view the available options) can be used to help in this process.

### Biological units

### Disulphide bonds



## Solvent molecules

## Prepare ligand for processing


## Checklist
