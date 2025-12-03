import pandas as pd
import os
from lisc import Counts1D

# ==========================================
# 1. SETUP & DEFINITIONS
# ==========================================
CSV_FILENAME = 'fMRI_sensory_data.csv'
FORCE_UPDATE = False

# Define Search Terms
base_term = '(fMRI OR functional magnetic resonance) AND hippocampus AND human'
sense_queries = {
    'Visual': f'{base_term} AND (visual OR vision OR sight)',
    'Auditory': f'{base_term} AND (auditory OR audition OR hearing)',
    'Olfactory': f'{base_term} AND (olfactory OR smell)',
    'Gustatory': f'{base_term} AND (gustatory OR taste)',
    'Tactile': f'{base_term} AND (tactile OR touch OR somatosensory)'
}
labels = list(sense_queries.keys())
# Extract the raw query strings
raw_terms = [sense_queries[k] for k in labels]
years = list(range(1990, 2025))

# ==========================================
# 2. DATA COLLECTION
# ==========================================

if os.path.exists(CSV_FILENAME) and not FORCE_UPDATE:
    print(f"✅ Found '{CSV_FILENAME}'. Loading data instantly...")
    df = pd.read_csv(CSV_FILENAME)

else:
    print(f"⚡ Starting data collection (1990-2024)...")
    print("   This will take a few minutes. Please wait.")

    data_list = []

    # MANUAL LOOP
    for year in years:
        print(f"   > Processing Year {year}...", end=" ")

        # We manually modify the query to include the specific year
        # This is very robust and prevents "hanging" on large hidden batches
        yearly_terms = [[f"{term} AND {year}[PDAT]"] for term in raw_terms]

        # Initialize LISC for this specific year
        c = Counts1D()
        c.add_terms(yearly_terms)

        try:
            # Run collection for this year
            c.run_collection(verbose=False)

            # Extract results
            for i, label in enumerate(labels):
                data_list.append({
                    'Year': year,
                    'Modality': label,
                    'Publications': c.counts[i]
                })
            print("Done.")

        except Exception as e:
            print(f"Error on {year}: {e}")

    # Create DataFrame and Save
    df = pd.DataFrame(data_list)
    print(f"💾 Saving data to '{CSV_FILENAME}'...")
    df.to_csv(CSV_FILENAME, index=False)
    print("✅ Success! Data saved.")