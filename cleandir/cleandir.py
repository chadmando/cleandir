import os
import shutil
from pathlib import Path


def main():
    path = get_path()
    files = list_dir(path)
    ext = get_extensions(files)
    make_folders(path, ext)
    copy_files(files, ext, path)


def get_path():
    input_path = input('enter an absolute path to clean (default={}): '.format(Path.cwd()))
    if input_path is not 'exit':

        if path.is_dir() and not 'exit':
            return path
        else:
            print('This is not a valid path. Please try again.')
            get_path()
    else:
        exit(code=0)

def list_dir(path):
    in_dir = Path.iterdir(path)
    files_in_dir = []
    for item in in_dir:
        if item.is_file():
            files_in_dir.append(item)

    return files_in_dir


def get_extensions(list_of_files):
    extensions = set()
    for file in list_of_files:
        if len(file.suffix) < 5:
            extensions.add(file.suffix)

    return extensions


def make_folders(path, subfolders):
    for item in subfolders:
        if not os.path.isdir(os.path.join(path, item)):
            os.mkdir(os.path.join(path, item))
            print('created folder in path {}'.format(os.path.join(path, item)))


def copy_files(files, ext_list, path):
    for file in files:
        base, sep, ext = file.partition('.')
        ext = str(ext).lower().strip()
        if ext in ext_list:
            try:
                shutil.copy2(os.path.join(path, file), os.path.join(path, str(ext).lower().strip(), file),
                             follow_symlinks=False)
            except shutil.SameFileError:
                print('an error occurred trying to move {}'.format(os.path.join(path, file)))


if __name__ == '__main__':
    main()
