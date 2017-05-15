
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
The PDB [example file]() is used as an example to illustrate the general process.

In this example we assume that you begin with a PDB containing all elements of the system.
Where multiple ligands are to be added to the same protein receptor then once the protein structure has been prepares once you can skip to the [ligand preparation](#prepare-ligand) section to create input for parameterization.

## Protein model



`pdb4amber` which is part of the AmberTools package (use the `--help` flag to view the available options) can be used to help in this process.


### Disulphide bonds



## Solvent molecules

## Prepare ligand for processing


## Checklist
