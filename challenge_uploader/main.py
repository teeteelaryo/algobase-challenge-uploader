import argparse
import os
import shutil
import subprocess

SUBMISSION_DIR = "submissions"

def ensure_submission_dir():
    if not os.path.exists(SUBMISSION_DIR):
        os.makedirs(SUBMISSION_DIR)

def submit_file(file_path, message):
    ensure_submission_dir()
    filename = os.path.basename(file_path)
    target_path = os.path.join(SUBMISSION_DIR, filename)
    shutil.copy(file_path, target_path)
    subprocess.run(["git", "add", target_path])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push"])
    print(f"Submitted {filename} with commit message: '{message}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a coding challenge solution to GitHub")
    parser.add_argument('--file', required=True, help='Path to the challenge solution')
    parser.add_argument('--message', required=True, help='Commit message')
    args = parser.parse_args()
    submit_file(args.file, args.message)
