# 🎬 Media File Integrity Checker

A Python tool that verifies the **integrity of media files** by checking whether the **last 2 seconds of each file are readable and error-free**, using FFmpeg.

---

## 🚀 What It Does

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

---

## 🧠 Why Check the Last 2 Seconds?

Media files that appear functional may still be:
- Incomplete (interrupted downloads)
- Truncated
- Partially corrupted at the end

This tool helps detect such issues before files are used in playback systems, backups, or data processing pipelines.

---

## 🛠️ Requirements

- Python 3.7+
- FFmpeg installed and accessible from the command line

Verify installation:

```bash
ffmpeg -version
```

---

## ▶️ Usage

1. Update the folder path in the script:

```python
folder_path = "/path/to/your/folder"
```

2. Run the script:

```bash
python script.py
```

The program will scan the directory, analyze each supported media file, and print a summary report indicating valid and problematic files.
