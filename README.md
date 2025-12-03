# Sensory Modality Trends in Hippocampal fMRI

This repository contains Python code to analyze the prominence of the five senses (Visual, Auditory, Olfactory, Gustatory, Tactile) in human hippocampal fMRI research from 1990 to 2024.

## Contents
* **01_collect_data.py**: Scrapes PubMed via LISC to generate yearly counts.
* **02_plot_trends.py**: Generates a line graph of research volume over time.
* **03_plot_composition.py**: Generates a stacked bar chart of sensory composition.
* **fMRI_sensory_data.csv**: The pre-collected dataset.

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run the plotting scripts: `python 02_plot_trends.py`
