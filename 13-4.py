from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    path = Path(path)
    for i in path.iterdir():
        if i.is_dir():
            folders.append (i.name)
        else:
            files.append (i.name)
    return files, folders      

print(parse_folder("C:\\Users\\rogulin\\Documents"))
