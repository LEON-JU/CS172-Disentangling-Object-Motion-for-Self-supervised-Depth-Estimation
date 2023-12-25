#!/bin/bash
#SBATCH -J test
#SBATCH -p debug
#SBATCH --cpus-per-task=4
#SBATCH --mail-type=all
#SBATCH --mail-user=xiaojx@shanghaitech.edu.cn
#SBATCH -N 1
#SBATCH -t 3:00
#SBATCH --gres=gpu:1
#SBATCH --output=%j.out
#SBATCH --error=%j.err
python -m dynamicdepth.train