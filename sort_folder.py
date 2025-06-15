import os
import shutil
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict

def copy_file(file: Path, target_dir: Path):
    ext = file.suffix[1:]  # remove dot
    if not ext:
        return
    target_ext_dir = target_dir / ext
    target_ext_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file, target_ext_dir / file.name)

def scan_directory(path: Path, file_list: list):
    for item in path.iterdir():
        if item.is_dir():
            scan_directory(item, file_list)
        elif item.is_file():
            file_list.append(item)

def main():
    source = Path(sys.argv[1])
    target = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')

    if not source.exists() or not source.is_dir():
        print("Source directory doesn't exist or is not a directory.")
        return

    all_files = []
    scan_directory(source, all_files)

    with ThreadPoolExecutor() as executor:
        for file in all_files:
            executor.submit(copy_file, file, target)

if __name__ == "__main__":
    main()
