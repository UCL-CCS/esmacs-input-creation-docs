
## RESP fitting (Antechamber)

Once the electrostatic potential has been successfully generated a two step process is used to convert this into RESP fitted charges.
In these commands the new options are; `-c` charge method and `cf` for charge filename. The '.ac' file is an intermediate file and most options are selct explanatory, except `-c wc` which simply means 'write out charge'.

```
antechamber -fi gout -fo ac -i 4bjx-ligand.out -o resp.ac -c resp
antechamber -fi ac -i resp.ac -c wc -cf resp.crg
```

## Create prep and frcmod files

The goal of the parameterization is to create two files used by Amber to read a a paremeterized drug.
The first is a *.prep* file which adds a new residues to the standard Amber residue database.
The other is a force field parameter modification, or *.frcmod*, file which lists parameters for bonds and other components of the forcefield that need to be added to characterize the ligand.

At this stage you need to consider a name for the ligand to be used in the simulation.
The residue name must be 3 characters long, in this example we use 'L01'.
BAC requires that this name in lowercase letters **must** be used consistently throughout the rest of the process to name all files associated with the ligand (for instance the *l01.prep* file generated below).

```
antechamber -i resp.ac -fi ac -c rc -cf resp.crg -o l01.prep -fo prepi -ao name -a 4bjx-ligand-h.pdb -fa pdb -rn L01
```

In this command, `-a` sets and additional file to be read for naming, `-ao name` means that only atom names are read from the input (rather than also including atom and bond types) and `-rn L01` sets the residue name.

Now we have the *.prep* file we need to use Antechamber to try and fill in any missing parameters in the force field by analogy to similar parameters which are present.
If Antechamber can't empirically calculate a value or has no analogy it will either add a default value that it thinks is reasonable or , in rare cases, insert a place holder.
This will contain zeros in all columns and be accompanied by the comment "ATTN: needs revision" in the output.
In these circumstances you will have to manually add these parameters.

```
parmchk -i l01.prep -f prepi -o l01.frcmod
```

Finally we need to produce a PDB which contains the ligand labelled using the new name we have given it.
An easy way of achieving this is to run the command:

```
sed 's/73B/L01/' 4bjx-ligand-h.pdb > l01.pdb
```

For use in BAC the ligand PDB (*l01.pdb* in the example) should be checked to ensure that it does not contain entries in the element column.
In particular entries for chlorine can be a problem.

## Check all is well
