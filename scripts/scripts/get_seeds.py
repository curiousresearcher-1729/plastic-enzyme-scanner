import pandas as pd
import os

# Verified PETase protein IDs from Uniprot
# These represent known 'plastic-eaters' we'll use for our search
seeds = {
    "A0A0K8P6T7": "Ideonella sakaiensis",
    "Q47QG3": "Thermobifida fusca",
    "A0A075B5G4": "Humicola insolens"
}

def create_seed_manifest():
    # Make sure the data directory exists
    if not os.path.exists('../data'):
        os.makedirs('../data')
        
    df = pd.DataFrame(list(seeds.items()), columns=['Accession', 'Species'])
    df.to_csv('../data/seed_manifest.csv', index=False)
    print("✅ Seed manifest created in data/ folder!")

if __name__ == "__main__":
    print("Running PlastiCore Data Acquisition...")
    create_seed_manifest()
