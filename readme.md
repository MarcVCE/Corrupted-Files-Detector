The script detects corrupted and tricky files (can be open but get frozen and stops in the middle of the playing), by
calculating and matching the last 2 seconds (for optimal processing (imagine if we have 100000 files)) with the final time length of the file, and shows the number of files per type (to see if they checked all the files you wanted) and names
the corrupted files.

Must have FFPMEG and Python installed. 