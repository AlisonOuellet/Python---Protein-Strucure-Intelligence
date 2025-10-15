# Python-Protein-Strucure-Intelligence
A Python tool that takes a protein (PDB ID) and automatically creates an interactive map of its structure, domains, interactions, and known mutations

Fonctionality:
- Automatically download the PDB file from RCSBIdentify domains (via InterPro or Pfam API)
- Analyze internal interactions (H-bonds, hydrophobic, salt bridges)
- Generate a PyMOL figure with automatic color coding (domains, mutations, chains, ligand, etc.)
- Export a publication-ready image + a mini PDF report
