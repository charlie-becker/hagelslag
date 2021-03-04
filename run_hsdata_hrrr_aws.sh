#!/bin/bash -l
#SBATCH --job-name=hsdata_wrfrt
#SBATCH --account=NAML0001
#SBATCH --ntasks=24
#SBATCH --cpus-per-task=1
#SBATCH --time=00:20:00
#SBATCH --partition=dav
#SBATCH --mem=64G
#SBATCH --output=aws_hsdata.out
#SBATCH --mail-type=ALL
conda activate hagelslag
python -u /glade/scratch/cbecker/hagelslag/bin/hsdata /glade/scratch/cbecker/hagelslag/config/HRRR_AWS_stream.config -p 1