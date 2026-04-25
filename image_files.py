import os
from PIL import Image
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

base_path = os.getcwd()
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")

# 1️⃣ Build full list of images
files_to_analyze = []
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.lower().endswith(valid_extensions):
            files_to_analyze.append(os.path.join(root, file))

# 2️⃣ Function to check one image
def is_corrupted(full_path):
    try:
        with Image.open(full_path) as img:
            img.load()
        return None
    except Exception:
        return full_path

# 3️⃣ Auto-detect number of threads
max_workers = min(32, (os.cpu_count() or 1) * 2)  # 2× núcleos, máximo 32 hilos

# 4️⃣ Analyze images in parallel
corrupted_files = []
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = {executor.submit(is_corrupted, path): path for path in files_to_analyze}
    for future in tqdm(as_completed(futures), total=len(futures), desc="Analyzing images", unit="image"):
        result = future.result()
        if result:
            corrupted_files.append(result)

# 5️⃣ Generate report
with open("corrupted_images_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Total images analyzed: {len(files_to_analyze)}\n")
    f.write(f"Corrupted images: {len(corrupted_files)}\n\n")
    f.write("=== LIST OF CORRUPTED IMAGES ===\n")
    for img in corrupted_files:
        f.write(f"{img}\n")

print("✅ Report generated: corrupted_images_report.txt")
