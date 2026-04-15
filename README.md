# PlastiCore: Functional Genomics for Plastic Degradation

## Project Overview
PlastiCore is a bioinformatics project designed to identify novel **PET-degrading enzymes** (PETases) from environmental metagenomic data. By combining evolutionary sequence analysis with modern computational tools, this project seeks to discover enzymes that can break down plastic waste more efficiently.

## The Goal
The primary objective is to move beyond simple sequence matching and use **Hidden Markov Models (HMMs)** to find "evolutionary cousins" of known plastic-eating enzymes that might have unique properties for industrial biotech applications.

## Tech Stack
* **Languages:** Python (Data Processing), R (Visualization)
* **Bioinformatics Tools:** HMMER, Prokka/Prodigal (Gene Prediction)
* **Workflow:** Nextflow (for reproducibility)
* **Environment:** Docker / Conda

## Project Structure
* `data/`: Sample metagenomic sequences (subsampled).
* `scripts/`: Python scripts for data cleaning and R scripts for phylogenetic trees.
* `results/`: Summary tables and high-resolution plots.
* `envs/`: Configuration files for software versions.

## How It Works (Planned)
1.  **Data Ingestion:** Fetching public metagenomic data from NCBI.
2.  **Gene Prediction:** Identifying Open Reading Frames (ORFs) in unknown sequences.
3.  **HMM Search:** Scoring sequences against a custom PETase profile.
4.  **Phylogenetic Mapping:** Visualizing where new hits sit on the tree of life.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
