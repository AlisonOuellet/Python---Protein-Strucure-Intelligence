# Python Protein Strucure Intelligence (PPSI)

**Protein-Structure-Intelligence 2025:** [https://protein_structure_inteligence](https://protein_structure_inteligence)  
![pipeline](https://img.shields.io/badge/pipeline-passed-brightgreen?style=flat-square)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
[![PyMOL](https://img.shields.io/badge/PyMOL-compatible-orange?style=for-the-badge)]()
![Status](https://img.shields.io/badge/status-active-success.svg)
![Last Commit](https://img.shields.io/github/last-commit/TON_UTILISATEUR/TON_REPO.svg)

---

### Overview
***Python Protein Structure Intelligence (PPSI)*** is a Python-based bioinformatics tool designed to automatically analyze and visualize protien 3D structures. It integrates domain annotation, structural interaction mapping, domains interactions, known mutations and publication visualization through **PyMOL** and biological databases.

This project aims to simplify **protein structure exploration** for researchers, educators, and students by automating the tedious steps of domain identification and structure analysis.

---

### Core Fonctionalities
- **Automated Structure Retrieval:** Fetches PDB structures directly from the RCSB Protein Data Bank.  
- **Domain Identification:** Uses **InterPro** and **Pfam APIs** to map functional domains.  
- **Interaction Analysis:** Detects hydrogen bonds, hydrophobic contacts, and salt bridges within or between chains.  
- **PyMOL Visualization:** Generates colored structural models (domains, ligands, chains, mutations).  
- **Exportable Reports:** Creates **publication-ready figures** and a concise **PDF summary report**.

---

### Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Example Output](#example-output)
4. [Project Structure](#project-structure)
5. [Credits](#credits)
6. [License](#license)

---

### Installation
```
# Clone the repository
git clone https://github.com/AlisonOuellet/Python---Protein-Strucure-Intelligence.git
cd Python---Protein-Strucure-Intelligence

# Create a virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate      # On Linux or macOS
venv\Scripts\activate         # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

---

### Usage

---

### Example Output

---

### Project Structure
```
Python-Protein-Structure-Intelligence/
│
├── main.py                 
├── modules/
│   ├── fetch_pdb.py      
│   ├── analyze_domains.py 
│   ├── interactions.py    
│   └── visualization.py   
│
├── results/              
├── requirements.txt
└── README.md
```

---

### Credits

---

## License
