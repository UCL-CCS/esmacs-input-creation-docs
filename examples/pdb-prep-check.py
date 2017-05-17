#! /usr/bin/env python

import os, sys
import argparse

# Amino acids recognized by Amber
aa = ["ACE", "ALA", "ARG", "ASH", "ASN", "ASP", "CYM", "CYS", "CYX", "GLH",
      "GLN", "GLU", "GLY", "HID", "HIE", "HIP", "HIS", "ILE", "LEU", "LYN",
      "LYS", "MET", "NHE", "NME", "PHE", "PRO", "SER", "THR", "TRP", "TYR",
      "VAL"]

def process_args():

    parser = argparse.ArgumentParser(
                    description='Check new system input files to be added to BAC store. Currently only works for single ligand systems.\n'
                    )

    parser.add_argument('-store', nargs='?', type=str,
                        help='BAC store where existing system information is held')

    parser.add_argument('-enzyme', nargs='?', type=str,
                        help='Enzyme to which the system should be added')

    parser.add_argument('-project', nargs='?', type=str,
                        help='Project to which the system should be added',
                        default='default')

    parser.add_argument('-ligname', nargs='?', type=str,
                        help='Residue ligname to check',
                        default='')

    parser.add_argument('-bacpdb', nargs='?', type=str, default='',
                        help='Name of PDB in BAC system description')

    parser.add_argument('-pdb_file', nargs='?', type=str, default='',
                        help='Path to input PDB file')

    parser.add_argument('-prep_file', nargs='?', type=str, default='',
                        help='Path to input AMBER prep file')

    return parser.parse_args()

def bac_pdb_to_ligand(filename):
    '''
    Read BAC formatted PDB file and extract ligand.
    BAC format specifies that the PDB should contain elements in the following
    order:
    protein, ligand, solvent
    This is assumed here, as is a single protein chain unless REMARK 6 records
    provided giving alternative number.

    filename (str): Path to file containing BAC format PDB

    returns: 
        ligname (str)
        ligand_atom_names (list)
        err (list)

    '''

    n_protein_chains = 1
    ligname = ''
    ligand_atom_names = []
    err = []
    warn = []

    protein_chain = {}

    with open(filename) as pdb_file:

        read_chains = 0

        for line in pdb_file:

            if line.startswith('REMARK   6'):

                cols = line.split()
                n_protein_chains = int(cols[-1])

            elif line.startswith('TER'):

                read_chains += 1

            elif read_chains == n_protein_chains:

                if line[0:6] in ['ATOM ', 'HETATM']:

                    if not ligname:

                        ligname = line[17:20].strip()

                    atom_name = line[12:15].strip()
                    ligand_atom_names.append(atom_name)

                    if not line[-2].strip():
                        if line.split()[-1] not in ['C','O','H','N']:
                            err.append('Blank characters at end of line:\n{0:s}'.format(line[:-1]))

                else:

                    err.append('Non ATOM line:\n{0:s}'.format(line[:-1]))

            elif read_chains < n_protein_chains:

                if line[17:20] not in aa:

                    resname = line[17:20]
                    chain = line[21]
                    resid = line[22:25].strip()

                    warn_txt = 'Non standard amino acid {0:s} at {1:s} {2:s}'.format(resname, chain, resid)

                    if warn_txt not in warn:
                        warn.append(warn_txt)
                pass

    return ligname, ligand_atom_names, err, warn


def get_prep_ligand_atoms(filename):
    """
    Extract ligand name and atom names from AMBER prep file.

    filename (str): Path to file containing BAC format PDB

    returns: 
        ligname (str)
        ligand_atom_names (list)
        err (list)

    """

    section = 'header'

    ligname = ''
    prep_atoms = []
    err = []

    with open(filename, 'r') as prep_file:

        header_count = 0

        for line in prep_file:

            if section == 'header':

                header_count += 1

                if header_count == 5:

                    ligname = line.split()[0]

                elif header_count == 7:
                    
                    section = 'atoms'

            elif len(line.strip()) == 0:

                pass
            
            elif line.startswith('LOOP'):

                section = 'loop'
            
            elif line.startswith('IMPROPER'):

                section = 'improper'

            elif section == 'atoms':

                cols = line.split()

                atom_name = cols[1]

                if atom_name != 'DUMM':
                    prep_atoms.append(atom_name)

                upper_name = atom_name.upper()

                if atom_name != upper_name:

                    err.append("Lower case letter in atom name {0:s}".format(atom_name))

    return ligname, prep_atoms, err

args = process_args()

if args.prep_file:

    prep_filename = args.prep_file

else:

    base_dir = os.path.join(args.store, 'system_descriptions')
    prep_dir = os.path.join(base_dir, args.project, 'drugs_par', args.enzyme, 'resp', args.ligname)
    prep_filename = os.path.join(prep_dir, args.ligname + '.prep')

    if not os.path.isfile(prep_filename):

        print "No prep file found or specified"
        sys.exit(1)

if args.pdb_file:

    pdb_filename = args.pdb_file

else:

    base_dir = os.path.join(args.store, 'system_descriptions')
    pdb_dir = os.path.join(base_dir, args.project, 'raw_pdbs', args.enzyme)
    pdb_filename = os.path.join(pdb_dir, args.bacpdb + '.pdb')

    if not os.path.isfile(pdb_filename):

        print "No pdb file found or specified"
        sys.exit(1)

prep_ligname, prep_atoms, prep_err = get_prep_ligand_atoms(prep_filename)

if args.ligname:
    if prep_ligname != args.ligname.upper():
        prep_err.append('Prep ligname, {0:s}, does not match expected name {1:s}'.format(prep_ligname, args.ligname))

pdb_ligname, pdb_atoms, pdb_err, pdb_warn = bac_pdb_to_ligand(pdb_filename)

if prep_ligname != pdb_ligname:
    pdb_err.append('Prep ligname, {0:s}, does not match name in PDB'.format(prep_ligname))

difference = set(pdb_atoms).difference(prep_atoms)

if not pdb_atoms:
    pdb_err.append('No ligand atoms found in PDB')

if difference:
    extra = ', '.join(difference)
    pdb_err.append('Following ligand atoms appear in PDB but not prep file ' + extra)

if not (pdb_err or prep_err):
    print "No errors"
    sys.exit(0)
else:

    print "Prep issues ({0:s}):".format(prep_filename)
    print "-"*25
    for err in prep_err:
        print err

    print ""
    print "PDB issues ({0:s}):".format(pdb_filename)
    print "-"*25
    for err in pdb_err:
        print err

    for warn in pdb_warn:
        print warn



