#
# Example file for working with os.path module
#

from datetime import date, datetime, time, timedelta

import os
import time


def main() -> None:
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print('Item exists: ' + str(os.path.exists('textfile.txt')))
    print('Item is a file: ' + str(os.path.isfile('textfile.txt')))
    print('Item is a directory: ' + str(os.path.isdir('textfile.txt')))

    # Work with file paths
    print('Item path: ' + str(os.path.realpath('textfile.txt')))
    print('Item path: ' + str(os.path.split(os.path.realpath('textfile.txt'))))

    # Get the modification time
    t = time.ctime(os.path.getmtime('textfile.txt'))
    print(t)
    print(datetime.fromtimestamp(os.path.getmtime('textfile.txt')))

    # Calculate how long ago the item was modified
    td = datetime.now() - datetime.fromtimestamp(os.path.getmtime('textfile.txt'))
    print('It has been ' + str(td) + ' since the file was modified')
    print('Or, ' + str(td.total_seconds()) + ' seconds')


if __name__ == '__main__':
    main()
