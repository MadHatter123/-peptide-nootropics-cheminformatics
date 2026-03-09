# Peptide Nootropics: Cheminformatics & BBB Penetration Analysis

## Project Overview
This project explores the **physicochemical properties of peptide-based nootropics** (Noopept, Semax, Selank, P21) and compares them with traditional small-molecule racetams. Using **RDKit** and **Python**, I analyzed molecular descriptors to understand why these compounds require different delivery methods (e.g., intranasal vs. oral).

## Key Objectives
*   Calculate molecular properties (MW, LogP, TPSA, HBD, HBA) for peptide nootropics.
*   Compare the **pharmacokinetic profiles** of peptides vs. small molecules (racetams).
*   Visualize the "BBB Penetration Gap" to explain the necessity of alternative delivery systems in neuropharmacology.

## Methodology
The analysis was performed using a custom Python script leveraging the following libraries:
*   `rdkit`: For advanced cheminformatics and molecular descriptor calculation.
*   `pandas`: For data manipulation and tabular representation.
*   `matplotlib` & `seaborn`: For high-quality data visualization.

### Analyzed Compounds
1. **Noopept:** A small peptide-like molecule (N-phenylacetyl-L-prolylglycine ethyl ester).
2. **Semax:** A fragment of ACTH (Met-Glu-His-Phe-Pro-Gly-Pro).
3. **Selank:** A synthetic analog of tuftsin (Thr-Lys-Pro-Arg-Pro-Gly-Pro).
4. **P21 (P021):** A neurogenic tetra-peptide derived from CNTF.

## Results & Findings

### 1. Physicochemical Properties Table
| Name | MW (g/mol) | LogP | TPSA (Å²) | HBD | HBA |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Noopept** | 318.37 | 1.14 | 75.63 | 1 | 4 |
| **Semax** | 813.93 | -4.32 | 318.01 | 10 | 13 |
| **Selank** | 751.88 | -5.41 | 285.02 | 10 | 12 |
| **P21 (P021)** | 578.57 | -3.12 | 234.01 | 8 | 10 |

### 2. Key Insights for Drug Discovery
*   **The BBB Barrier:** While racetams (MW < 250, TPSA < 70) easily cross the Blood-Brain Barrier via passive diffusion, large peptides like **Semax** and **Selank** have massive TPSA (> 280 Å²) and negative LogP values. This scientifically explains why they are administered **intranasally** to bypass the BBB via the olfactory pathway.
*   **Noopept's Hybrid Profile:** Noopept bridges the gap between peptides and small molecules. Its relatively low TPSA and positive LogP allow for oral bioavailability, unlike larger peptides.
*   **Molecular Complexity:** The high number of Hydrogen Bond Donors (HBD) and Acceptors (HBA) in peptides significantly increases their polarity, making them highly hydrophilic and challenging for traditional oral drug delivery.

## Visualization
The project includes a comparison plot (`nootropics_comparison_plot.png`) that maps the "Ideal CNS Penetration Zone" vs. the "Peptide Zone," providing a clear visual representation of the pharmacokinetic challenges in neuropeptide therapy.

## How to Run
1. Ensure you have Python 3.x installed.
2. Install dependencies: `pip install rdkit pandas matplotlib seaborn`.
3. Run the analysis script: `python calculate_peptides.py`.
4. Generate the comparison plot: `python visualize_comparison.py`.

---
*This project was developed as part of a professional portfolio for Pharmaceutical R&D roles.*
