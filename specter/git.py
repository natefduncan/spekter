import os
from dulwich import porcelain
from pathlib import Path
from utils import get_all_files

from dotenv import load_dotenv
load_dotenv()

HOST=os.getenv("HOST")
REPO=os.getenv("REPO")
USERNAME=os.getenv("USERNAME")
PASSWORD=os.getenv("PASSWORD")

def create_new_repo(path): 
    repo = porcelain.init(path)
    return repo

def clone_repo(url, path):
    porcelain.clone(url, path)

def get_repo(path):
    repo = porcelain.init(path)
    return repo

def commit(repo, files):
    for file in files:
        porcelain.add(repo, files)
        porcelain.commit(repo, b"Automated commit")

def push(repo):
    r = porcelain.push(repo.path, f"{USERNAME}@{HOST}:{REPO}", "master")

def pull(repo):
    r = porcelain.pull(repo.path, f"{USERNAME}@{HOST}:{REPO}")

if __name__=="__main__":
    home_dir = Path(os.path.expanduser('~'))
    files = get_all_files(f"{str(home_dir)}/Documents/Notes", ignore=[".DS_Store", "/data", "/.git", "sonic.cfg"])
    repo = get_repo(f"{str(home_dir)}/Documents/Notes")
    relative_files = ["." + file.replace(repo.path, "") for file in files]
    commit(repo, files)
    push(repo)
