import shutil
from pathlib import Path


def main():
    """Program prompts user for an folder or directory to clean. Get the contents of the folder and created subfolders
    based on common file extension contained within.  A subfolder is created for each extension and files are moved or
    copied into the subfolders."""
    path = get_path_to_clean()
    files = list_dir(path)
    ext = get_extensions(files)
    make_folders(path, ext)
    copy_files(files, ext)


def get_path_to_clean():
    """Prompt user for directory to clean.  'exit' will exit program.  No input selects the current working dir"""
    global path_to_clean
    input_path = input('enter an absolute path to clean, or "exit" (default path={}): '.format(Path.cwd()))
    if input_path.lower() == 'exit':
        exit(code='user initiated exit')
    if input_path == '':
        path_to_clean = Path.cwd().absolute()

    path_to_clean = Path(input_path)
    print("You want to clean this folder: {}".format(str(path_to_clean)))
    if path_to_clean.is_dir():
        return path_to_clean
    else:
        print('\n This is not a valid path. Please try again. \n')
        get_path_to_clean()


def list_dir(path):
    """ Funtion take a Path object and returns all files in the folder."""
    in_dir = Path.iterdir(path)
    files_in_dir = []
    for item in in_dir:
        if item.is_file():
            files_in_dir.append(item)

    return files_in_dir


def get_extensions(list_of_files):
    """Function take a list of Path object and adds the file extenstion/suffix to a set. The set of extensions
    are returned"""
    extensions = set()
    for file in list_of_files:
        if len(file.suffix) < 6:
            extensions.add((file.suffix).lstrip('.'))

    return extensions


def make_folders(path, subfolders):
    """Takes a Path object and a list of desired subfolders.  Creates the subfolders in the path. Nothing returned. """
    for item in subfolders:
        Path.mkdir(Path.joinpath(path, item), exist_ok=True)
        print('created folder in path {}'.format(Path.joinpath(path, item)))


def copy_files(files, ext_list):
    """Takes a list of Path objects and a set of extensions. If the file's suffix is in the list, the file
      is copied into a subfolder whose name is the extension. The result is all files in the list with the same extension
      into subfolders based on extension. """
    for file in files:
        ext = (file.suffix).lstrip('.')

        if ext in ext_list:
            src = str(file)
            dest = Path(file.parents[0]).joinpath(ext, file.name)
            print("Destination path is {}".format(dest))
            try:
                shutil.copy2(src, dest, follow_symlinks=False)
            except shutil.SameFileError as e:
                print(e)


if __name__ == '__main__':
    main()
