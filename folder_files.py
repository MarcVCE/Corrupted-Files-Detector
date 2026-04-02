import os

base_path = os.getcwd()
errors = set()  # set to avoid duplicates

for root, dirs, files in os.walk(base_path, topdown=True):
    for d in dirs:
        full_path = os.path.join(root, d)
        try:
            os.listdir(full_path)
        except Exception:
            errors.add(d)

# Save only folder names
with open("folders_with_errors.txt", "w", encoding="utf-8") as f:
    for name in sorted(errors):
        f.write(name + "\n")

print(f"Total folders with errors: {len(errors)}")
print("Saved to folders_with_errors.txt")