import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load both datasets
df_racetams = pd.read_csv('racetams_properties.csv')
df_peptides = pd.read_csv('peptides_properties_final.csv')

# Add a Class column
df_racetams['Class'] = 'Racetams'
df_peptides['Class'] = 'Peptides'

# Combine
df_all = pd.concat([df_racetams, df_peptides], ignore_index=True)

# Set the style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 10))

# Create the scatter plot
scatter = sns.scatterplot(
    data=df_all, 
    x='TPSA', 
    y='XLogP', 
    size='MolecularWeight', 
    hue='Class', 
    style='Class',
    palette='Set1', 
    sizes=(100, 1000),
    alpha=0.7
)

# Add labels for each point
for i in range(df_all.shape[0]):
    plt.text(
        df_all.TPSA[i]+5, 
        df_all.XLogP[i]+0.1, 
        df_all.Name[i], 
        fontsize=9, 
        weight='bold'
    )

# Highlight the "Ideal CNS Penetration Zone"
plt.axvspan(0, 70, color='green', alpha=0.1, label='Ideal CNS Zone (TPSA < 70)')
plt.axhspan(0, 3, color='blue', alpha=0.05, label='Ideal CNS Zone (LogP > 0)')

# Add titles and labels
plt.title('Nootropics Comparison: Racetams vs. Peptides', fontsize=18, pad=20)
plt.xlabel('Topological Polar Surface Area (TPSA, Å²)', fontsize=14)
plt.ylabel('Lipophilicity (XLogP)', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Drug Class')

# Add annotations
plt.text(200, 1, "Peptides often fall outside\nthe 'Ideal CNS Zone' due to\nhigh polarity and size,\nrequiring alternative delivery\n(e.g., intranasal).", 
         bbox=dict(facecolor='white', alpha=0.5), fontsize=11)

plt.tight_layout()
plt.savefig('nootropics_comparison_plot.png', dpi=300)
print("Comparison visualization saved as nootropics_comparison_plot.png")
