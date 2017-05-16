
## Combine component PDBs

As noted earlier BAC expects the PDB to have a set structure - protein, lgand and then solvent.
It also expects `TER` cards between chains.


Be careful to ensure that any `END` cards only appear as the very last line of the file.

## Add header

Additionally, a BAC specific header should be included at the top of the file.
This simply contains the number of protein chains included.

```
REMARK   6 PROTEIN CHAINS 1
```

As the PDB format is based on columns the `REMARK   6 PROTEIN CHAINS ` section (up to the figure for the number of protein chains) must be reproduced exactly.

## Organize files and create tarball

```
mkdir l01
```

Copy the *.frcmod* and *prep files* into this directory.

```
cp l01.frcmod l01
cp l01.prep l01
```

Finally, we create a tarball containing the directory we created:

```
tar cfv bet-l01.tar l01
```

The two inputs needed for use in the ufBAC are thus the full system PDB (*bet-l01.pdb*) and this tarball of the ligand parameterization (*bet-l01.tar*).
