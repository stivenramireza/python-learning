#
# Example file for working with filesystem shell methods
#

from zipfile import ZipFile

import os
import shutil


def main() -> None:
    # Make a duplicate of an existing file
    if os.path.exists('textfile.txt'):
        # Get the path to the file in the current directory
        src = os.path.realpath('textfile.txt')

        # Let's make a backup copy by appending "bak" to the name
        dst = src + '.bak'

        # Copy over the permissions, modification times, and other info
        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        # Rename the original file
        # os.rename('textfile.txt', 'newfile.txt')

        # Now put things into a ZIP archive
        root_dir, tail = os.path.split(src)
        shutil.make_archive('archive', 'zip', root_dir)

        # More fine-grained control over ZIP files
        with ZipFile('testzip.zip', 'w') as new_zip:
            new_zip.write('textfile.txt')
            new_zip.write('textfile.txt.bak')


if __name__ == '__main__':
    main()
