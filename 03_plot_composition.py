import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import os

# 1. LOAD DATA
# -----------------------------------------------------------------------------
CSV_FILENAME = 'fMRI_sensory_data.csv'

if not os.path.exists(CSV_FILENAME):
    print("⚠️ Data file not found! Please run the data collection script first.")
else:
    df = pd.read_csv(CSV_FILENAME)

    # 2. PREPARE DATA FOR STACKED PLOT
    # -----------------------------------------------------------------------------
    # Pivot to Wide Format: Rows=Years, Columns=Modalities
    df_pivot = df.pivot(index='Year', columns='Modality', values='Publications')

    # Sort columns by total volume so the stack order is consistent
    column_order = df_pivot.sum().sort_values(ascending=False).index
    df_pivot = df_pivot[column_order]

    # 3. PLOT CONFIGURATION (Journal Style)
    # -----------------------------------------------------------------------------
    sns.set_theme(style="white", context="paper")

    # Use the consistent Colorblind palette
    colors = sns.color_palette("colorblind", n_colors=len(df_pivot.columns))

    mpl.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'axes.linewidth': 1.0,
    })

    fig, ax = plt.subplots(figsize=(10, 6))

    # 4. CREATE THE STACKED BAR PLOT
    # -----------------------------------------------------------------------------
    df_pivot.plot(
        kind='bar',
        stacked=True,
        color=colors,
        width=0.85,
        ax=ax,
        edgecolor='black',
        linewidth=0.5
    )

    # 5. SCIENTIFIC DETAILING
    # -----------------------------------------------------------------------------
    # Title & Labels
    ax.set_title('Annual Composition of Sensory Research in Hippocampal fMRI (1990-2024)',
                 fontweight='bold', pad=20)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Publications')

    # Fix X-Axis Labels (Show every 5th year only)
    tick_labels = [str(year) if i % 5 == 0 else '' for i, year in enumerate(df_pivot.index)]
    ax.set_xticklabels(tick_labels, rotation=0)

    # Clean Grid & Legend
    ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='gray')
    ax.xaxis.grid(False)
    ax.legend(title="Modality", frameon=False, loc='upper left')

    sns.despine(trim=False)
    plt.tight_layout()

    # 6. SAVE THE PLOT

    print("Saving figures...")

    plt.savefig('sensory_fMRI_human_hippo_boxplot.png', dpi=300, bbox_inches='tight')


    print("✅ Saved to 'sensory_composition_plot.png'")

    # Show the plot
    plt.show()