import os
from challenge_uploader import main

def test_ensure_submission_dir():
    main.ensure_submission_dir()
    assert os.path.exists("submissions")
