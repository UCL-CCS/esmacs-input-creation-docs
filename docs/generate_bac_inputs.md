
## Combine component PDBs

As noted earlier BAC expects the PDB to have a set structure - protein, ligand and then solvent.
It also expects `TER` cards between chains.
During this tutorial we have prepared files for each of these sections, edited to meet the requirements of Amber and BAC:

* Protein: 4bjx-protein-stripped.pdb
* Ligand: l01.pdb
* Solvent: 4bjx-solvent.pdb

If all three files have been properly prepared the combination of the sections can be as simple as:

```
cat 4bjx-protein-stripped.pdb l01.pdb 4bjx-solvent.pdb > bet-l01.pdb
```

When naming the final PDB it is helpful to use a meaningful name.
Here *bet-l01.pdb* combines the protein name (it is a BRD4 structure, these are members of the Bromo-and Extra-Terminal domain, BET, family) and the ligand name.

Check this PDB to ensure that there is a line containing only the text `TER` between the protein, ligand and solvent sections of the file.
Be careful to ensure that any `END` cards only appear as the very last line of the file (hint: you need to change an `END` into a `TER` in the file as generated above).

## Add header

Additionally, a BAC specific header should be included at the top of the file.
This simply contains the number of protein chains included.

```
REMARK   6 PROTEIN CHAINS 1
```

As the PDB format is based on columns the `REMARK   6 PROTEIN CHAINS ` section (up to the figure for the number of protein chains) must be reproduced exactly.

The protein used here contains only one chain, so edit *bet-l01.pdb* file accordingly.
An example PDB file can be dowloaded from [here](docs/examples/bet-l01.pdb).

## Organize files and create tarball

For upload into BAC a particular arrangement of files is needed.

Create a directory, named using the lowercase version of the ligand residue name:

```
mkdir l01
```

Copy the *.frcmod* and *prep files* into this directory.

```
cp l01.frcmod l01
cp l01.prep l01
```

Finally, create a tarball containing the directory we created:

```
tar cfv bet-l01.tar l01
```

An example tarball can be downloaded [here](examples/l01.tar). 
The two inputs needed for use in the ufBAC are thus the full system PDB (*bet-l01.pdb*) and this tarball of the ligand parameterization (*bet-l01.tar*).

In the next section we detail the use of scripts to check that the inputs created are ready for successful use in BAC.
