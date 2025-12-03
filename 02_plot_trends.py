import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


sns.set_theme(style="ticks", context="paper")

mpl.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.linewidth': 1.0,
    'grid.color': '#E0E0E0',
})

plt.figure(figsize=(8, 5))
ax = plt.gca()

sns.lineplot(
    data=df,
    x='Year',
    y='Publications',
    hue='Modality',
    palette="colorblind",
    linewidth=2.0,
    ax=ax
)

ax.set_title('Sensory Modality Trends in Human Hippocampal fMRI Research',
             fontweight='bold', pad=15)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Publications')

ax.yaxis.grid(True, linestyle='-', linewidth=0.5)
ax.xaxis.grid(False)
ax.tick_params(direction='out', length=4, width=1)
ax.set_xlim(df['Year'].min(), df['Year'].max())
ax.set_ylim(bottom=0)

handles, plt_labels = ax.get_legend_handles_labels()
ax.legend(handles, plt_labels, title="", loc='upper left', frameon=False)

sns.despine(trim=False)
plt.tight_layout()
print("Saving figures...")

plt.savefig('sensory_fMRI_human_hippo_plot.png', dpi=300, bbox_inches='tight')

print("✅ Saved to 'sensory_composition_plot.png'")

# Show the plot
plt.show()