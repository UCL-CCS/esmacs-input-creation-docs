In many systems there are extra non-standard residues that bind along side a ligand.
There are (limited) capabilities for handling these within BAC.

## Cofactors

The first step is to parameterize the cofactor just as described previously for the ligand. 
This should provide you with a *prep*, *frcmod* and matching *PDB* file.
The *prep* file then needs to be converted into an Amber *lib* file.
This is done using tLeap and a script similar to the following (you need to edit the filenames to match the *prep*, *frcmod* and *PDB* files you generated):

```
loadamberprep sam.prep
SAM = loadpdb sam-h.pdb
loadamberparams sam.frcmod
saveoff SAM sam.lib
```

Now make copies of the *lib* and *frcmod* files named *COFACTOR.lib* and *COFACTOR.frcmod*.

These should be added to the top level of the tarball containing the ligand parameters.
So that for the [tarball](examples/cofactor.tar) contents for a cofactor and a ligand called 4ZX would look like:

```
COFACTOR.lib
COFACTOR.frcmod
4zx/4zx.frcmod
4zx/4zx.prep
```

