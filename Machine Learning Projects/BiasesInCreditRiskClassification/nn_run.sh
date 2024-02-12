#!/bin/bash
#SBATCH --job-name "nn-train"
#SBATCH --mem 32G

# change filename below
python3 nn_run.py
