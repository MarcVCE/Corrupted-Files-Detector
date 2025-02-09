import os
import subprocess
import re
from collections import defaultdict

def get_duration(filepath):
    """ Gets the duration of the file in seconds using FFmpeg. """
    cmd = ["ffmpeg", "-i", filepath]
    result = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    
    match = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", result.stderr)
    if match:
        hours, minutes, seconds = map(float, match.groups())
        return hours * 3600 + minutes * 60 + seconds  # Convert to seconds
    return None  # Could not retrieve duration

def check_last_2_seconds(directory):
    """ Scans folders and subfolders, verifying the last 2 seconds and counting files by type and status. """
    file_count = defaultdict(int)  # File counter by type
    valid_files = 0  # Counter for valid files
    corrupted_files = []  # List of problematic files

    for root, _, files in os.walk(directory):  # Traverse folders and subfolders
        for filename in files:
            filepath = os.path.join(root, filename)
            ext = filename.lower().split('.')[-1]  # Extract file extension

            if ext in {'mp4', 'mkv', 'avi', 'mp3', 'wav', 'flac', 'mov', 'webm'}:
                file_count[ext] += 1  # Count file by type
                print(f"🔍 Checking the last 2s of: {filepath}")

                duration = get_duration(filepath)
                if not duration or duration < 2:
                    print(f"⚠️ Could not retrieve duration or file is too short.")
                    corrupted_files.append(filepath)
                    continue

                # Verify if the file actually ends correctly
                cmd = [
                    "ffmpeg", "-v", "error",
                    "-sseof", "-2",  # Try playing from 2s before the end
                    "-i", filepath,
                    "-f", "null", "-"
                ]
                
                try:
                    result = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
                    errors = result.stderr.lower()

                    if errors:
                        print(f"⚠️ Issue found in {filepath}:")
                        if "corrupt" in errors or "decode error" in errors:
                            print("❌ Corrupt or unreadable file.")
                        elif "invalid data" in errors:
                            print("❌ Invalid data in the last 2 seconds.")
                        elif "packet corrupt" in errors:
                            print("⚠️ Packet corruption, possible playback issue.")
                        elif "end of file" in errors or "unexpected eof" in errors:
                            print("⚠️ Abrupt cut before the expected end.")
                        else:
                            print(errors)  # Show any other uncategorized errors
                        corrupted_files.append(filepath)
                    else:
                        print(f"✅ {filename} is fine.")
                        valid_files += 1

                except Exception as e:
                    print(f"❌ Error processing {filename}: {e}")
                    corrupted_files.append(filepath)

    # Display final summary
    print("\n📊 Summary of detected files:")
    for ext, count in sorted(file_count.items()):
        print(f"  - {count} {ext.upper()}")

    print("\n✅ Valid files:", valid_files)
    print("❌ Corrupt files:", len(corrupted_files))

    if corrupted_files:
        print("\n⚠️ List of problematic files:")
        for file in corrupted_files:
            print(f"  - {file}")

# Change this path to the root folder where your files are located
folder_path = "/path/to/your/folder"
check_last_2_seconds(folder_path)
