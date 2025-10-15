# Fetches PDB structures from RCSB PDB and saves them locally.
from rcsbapi.data import DataQuery as Query

def fetch_pdb(pdb_ids):
    query = Query(
        input_type = "entries",
        input_ids = ["1TUP"],
        return_data_list=["exptl.method"]
    )

    return query.exec()

# https://rcsbapi.readthedocs.io/en/latest/
# https://data.rcsb.org/index.html#data-api 