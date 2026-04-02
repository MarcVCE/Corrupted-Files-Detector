import os
from PIL import Image
from tqdm import tqdm

base_path = os.getcwd()
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")

# 1️⃣ Build full list of images
files_to_analyze = []
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.lower().endswith(valid_extensions):
            files_to_analyze.append(os.path.join(root, file))

# 2️⃣ Analyze all images with progress bar
corrupted_files = []
for full_path in tqdm(files_to_analyze, desc="Analyzing all images", unit="image"):
    try:
        with Image.open(full_path) as img:
            img.load()
    except Exception:
        corrupted_files.append(full_path)

# 3️⃣ Generate report
with open("corrupted_images_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Total images analyzed: {len(files_to_analyze)}\n")
    f.write(f"Corrupted images: {len(corrupted_files)}\n\n")
    f.write("=== LIST OF CORRUPTED IMAGES ===\n")
    for img in corrupted_files:
        f.write(f"{img}\n")

print("✅ Report generated: corrupted_images_report.txt")