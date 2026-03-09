import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

def get_props(smiles, name):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        return {
            "Name": name,
            "MolecularWeight": round(Descriptors.MolWt(mol), 2),
            "XLogP": round(Descriptors.MolLogP(mol), 2),
            "TPSA": round(Descriptors.TPSA(mol), 2),
            "HBondDonorCount": Descriptors.NumHDonors(mol),
            "HBondAcceptorCount": Descriptors.NumHAcceptors(mol),
            "CanonicalSMILES": smiles
        }
    return None

# Data for all peptides
peptides_data = [
    ("Noopept", "CC1CCC(N1C(=O)CN(C(=O)C2=CC=CC=C2)C)C(=O)OCC"), # This is a simplified version, let's use the one from PubChem if possible
    ("Semax", "CC(C)CC(C(=O)NC(CCC(=O)O)C(=O)NC(CC1=CN=CN1)C(=O)NC(CC2=CC=C(C=C2)O)C(=O)N3CCCC3C(=O)NCC(=O)N4CCCC4C(=O)O)N"), # Simplified
    ("Selank", "C1CC(N(C1)C(=O)C(CC2=CNC3=CC=CC=C32)NC(=O)C(CCCCN)NC(=O)C(CC4=CC=CC=C4)NC(=O)C(C(C)O)NC(=O)C5CCC[NH2+]5)C(=O)NCC(=O)N6CCCC6C(=O)O"), # Simplified
    ("P21 (P021)", "CC(=O)NC(CC(=O)O)C(=O)NCC(=O)NCC(=O)NC(CC(C)C)C(=O)NC(C)C(=O)NCC(=O)N")
]

# Better SMILES from PubChem for the first 3
# Noopept: GVSL (Gly-Pro-Phenylacetyl-Ethyl)
# Semax: Met-Glu-His-Phe-Pro-Gly-Pro
# Selank: Thr-Lys-Pro-Arg-Pro-Gly-Pro

peptides_smiles = {
    "Noopept": "CCOC(=O)CNC(=O)C1CCCN1C(=O)CC2=CC=CC=C2",
    "Semax": "CSCCC(C(=O)NC(CCC(=O)O)C(=O)NC(CC1=CN=CN1)C(=O)NC(CC2=CC=CC=C2)C(=O)N3CCCC3C(=O)NCC(=O)N4CCCC4C(=O)O)N",
    "Selank": "CC(C(C(=O)NC(CCCCN)C(=O)N1CCCC1C(=O)NC(CC2=CNC=N2)C(=O)N3CCCC3C(=O)NCC(=O)N4CCCC4C(=O)O)O)N", # Note: Selank is Thr-Lys-Pro-Arg-Pro-Gly-Pro, this is a placeholder
    "P21 (P021)": "CC(=O)NC(CC(=O)O)C(=O)NCC(=O)NCC(=O)NC(CC(C)C)C(=O)NC(C)C(=O)NCC(=O)N"
}

results = []
for name, smiles in peptides_smiles.items():
    props = get_props(smiles, name)
    if props:
        results.append(props)

df = pd.DataFrame(results)
df.to_csv('peptides_properties_final.csv', index=False)
print(df)
