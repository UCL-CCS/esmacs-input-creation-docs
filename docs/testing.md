Incorrectly formatted PDB or prep files should be caught by ufBAC but it is worth checking the system is correctly set up before uploading your inputs.
In this section we use a script to check the basic input we have generated and provide a checklist of the major points that you should check in your PDB and ligand parameters files.

## Check PDB and *.prep* file for errors

Download the short Python 2 script [pdb-prep-check.py](examples/pdb-prep-check.py).
This script is designed to ensure that the PDB and prep file are compatible with BAC and that the ligand structure is named in accordance with the topology.

To run the script use the command:

```
python pdb-prep-check.py -pdb_file bet-l01.pdb -prep_file l01.prep
```

The output will provide information on lines where issues may arise and hints on how to correct them.

### Checklist

*  Ensure PDB follows the BAC format:
   -  Header line describing number of protein chains
   -  Chains ordered; protein, ligand, solvent
   -  All chains end with TER cards
*  Ensure that the PDB header line matches the number of protein chains
*  Make sure the only END line is the last line of the file
*  Do not use the element column for ligand atoms
