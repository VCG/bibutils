source ~/anaconda3/etc/profile.d/conda.sh
conda activate bibutils
python coi.py --first Hanspeter --last Pfister
git add .
git commit -m "... updated conflict of interest for Hanspeter Pfister"
git push
conda deactivate