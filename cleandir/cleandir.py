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
    if input_path.lower() is 'exit':
        exit(code=0)

    path = Path(input_path)
    if path.is_dir():
        return path
    else:
        print('This is not a valid path. Please try again.')
        get_path()


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
        if len(file.suffix) < 6:
            extensions.add((file.suffix).lstrip('.'))

    return extensions


def make_folders(path, subfolders):
    for item in subfolders:
        Path.mkdir(Path.joinpath(path, item), exist_ok=True)
        print('created folder in path {}'.format(Path.joinpath(path, item)))


def copy_files(files, ext_list, path):
    for file in files:
        ext = (file.suffix).lstrip('.')

        if ext in ext_list:
            src = str(file)
            d = Path(file.parents[0]).joinpath((str(ext)), (file.name()))
            print(type(d))
            try:
                shutil.copy2(src, dest, follow_symlinks=False)
            except shutil.SameFileError as e:
                print(e)


if __name__ == '__main__':
    main()
