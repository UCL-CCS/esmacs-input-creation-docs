
## Protein model



1. All chains to be included in the final model must have coordinates present (BIOMT records, etc. will not be applied)
2. The sequenc must contain unambiguous coordinates for each residue and atom (i.e. no alternative locations or residues)
3. All hydrogen atoms should be removed
3. Chains must contain no gaps and residues numbered sequentially
4. Each chain must have a unique ID and end with a TER card
5. Solvent molecules must follow all protein chains
6. The ligand should be removed from the structure at this stage

Additionally, a BAC specific header should be included at the top of the file.
This simply contains the number of protein chains included.

```
REMARK   6 PROTEIN CHAINS 1
```

As the PDB format is based on columns the `REMARK   6` section must be reproduced exactly.

## Extract ligand



## Add hydrogens

## Checklist
