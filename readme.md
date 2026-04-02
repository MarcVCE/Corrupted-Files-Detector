# 🎬 Media File Integrity Checker

A set of Python tools that verify the **integrity of media files, images, and folder structure**, detecting corruption and access errors before they cause problems in backups, pipelines, or playback systems.

---

## 📦 Scripts

### 🎥 `video_files.py` — Video & Audio Integrity Check

Verifies that the **last 2 seconds of each media file are readable and error-free**, using FFmpeg.

- Recursively scans a directory and its subdirectories.
- Detects supported media formats:
  - Video: `mp4`, `mkv`, `avi`, `mov`, `webm`
  - Audio: `mp3`, `wav`, `flac`
- Retrieves total file duration via FFmpeg.
- Attempts to decode the last 2 seconds of each file.
- Detects issues such as:
  - Corrupted files
  - Decode errors
  - Invalid data
  - Unexpected end-of-file (EOF)
- Generates a summary including:
  - File count by extension
  - Number of valid files
  - List of problematic files

> **Why check the last 2 seconds?** Media files that appear functional may still be incomplete (interrupted downloads), truncated, or partially corrupted at the end.

---

### 🖼️ `image_files.py` — Image Integrity Check

Scans for **corrupted image files** using Pillow, attempting to fully load each image into memory.

- Recursively scans a directory for image files.
- Supports: `jpg`, `jpeg`, `png`, `bmp`, `gif`, `tiff`
- Shows a progress bar during analysis (`tqdm`).
- Generates a report `corrupted_images_report.txt` with:
  - Total images analyzed
  - Number of corrupted images
  - Full paths of all corrupted files

---

### 📁 `folder_files.py` — Folder Access Error Check

Detects **folders that cannot be listed** due to permission or filesystem errors.

- Recursively walks the current working directory.
- Attempts to list the contents of each subfolder.
- Collects the names of any folders that raise an exception.
- Saves results to `folders_with_errors.txt` (deduplicated and sorted).

---

## 🛠️ Requirements

- Python 3.7+
- [FFmpeg](https://ffmpeg.org/) installed and accessible from the command line (required for `video_files.py`)
- Python packages: `Pillow`, `tqdm` (required for `image_files.py`)

Verify FFmpeg installation:

```bash
ffmpeg -version
```

Install Python dependencies:

```bash
pip install Pillow tqdm
```

---

## ▶️ Usage

### `video_files.py`

1. Update the folder path in the script:

```python
folder_path = "/path/to/your/folder"
```

2. Run the script:

```bash
python video_files.py
```

### `image_files.py`

Run from the directory you want to scan (uses `os.getcwd()` as base path):

```bash
python image_files.py
```

Output: `corrupted_images_report.txt`

### `folder_files.py`

Run from the directory you want to scan (uses `os.getcwd()` as base path):

```bash
python folder_files.py
```

Output: `folders_with_errors.txt`
