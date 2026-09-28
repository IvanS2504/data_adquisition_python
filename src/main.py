import os

print("Generating dataset...")
os.system("python src/generation.py")

print("Running adquisition and analysis...")
os.system("python src/adquisition.py")
