#!/usr/bin/env python2

from __future__ import print_function

import os
import sys
from datetime import datetime
from socket import gethostname


TIME_FORMAT = "%b %d, %Y %H:%M:%S"
LINE_FORMAT = "%(time)s\t%(hostname)s\t%(curdir)s\t%(message)s"
LOG_FILE    = "~/time.log"


def main():
    # All arguments except our program name are the notes.
    notes = ' '.join(sys.argv[1:])
    if len(notes) == 0:
        notes = '<no message>'

    # Format time.
    time = datetime.now().strftime(TIME_FORMAT)

    # If the current dir is in our home dir, collapse it.
    home_dir = os.path.expanduser('~')
    curr_dir = os.path.abspath(os.curdir)
    if curr_dir.startswith(home_dir):
        # Strip off the home dir and path seperator
        curr_dir = curr_dir[len(home_dir)+1:]

        # Properly join home dir
        curr_dir = os.path.join('~', curr_dir)

    # Get other info.
    meta = {
        'message': notes,
        'time': time,
        'hostname': gethostname(),
        'curdir': curr_dir,
    }

    # Format
    line = LINE_FORMAT % meta

    # Append to file.
    with open(os.path.expanduser(LOG_FILE), 'ab') as f:
        f.write(line + '\n')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
