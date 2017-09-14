###
### This script ot designed to be run on the directory downloaded from D2L with all submissions.
### This was originally written for CS 110, Summer 2017.
###

import re
import sys
import argparse
import os
import shutil
import unicodedata

parser = argparse.ArgumentParser(description='Grading Helper')
parser.add_argument('--idir', required=True,
    help='Directory downloaded from D2L to process.')
parser.add_argument('--odir', required=True,
    help='Directory to put output in')
args = parser.parse_args()

bp = os.path.basename(os.path.normpath(args.idir))

submission_re = r'([0-9-]+) - ([ \-A-Za-z\w]+)- ([A-Za-z]+) ([0-9]+), ([0-9]+) ([0-9]+) ([AP]M) - ([\-_A-Za-z0-9\.]+)'
directory_re = r'([A-Za-z0-9]+) (Download) ([A-Za-z]+) ([0-9]+), ([0-9]+) ([0-9]+) ([AP]M)'

if os.path.exists(args.odir):
    print(args.odir + ' Already exists! You have been warned.')

if not os.path.exists(args.odir):
    os.makedirs(args.odir)

for fn in os.listdir(args.idir):
    f = os.path.join(args.idir, str(fn))
    if os.path.isfile(f) and fn != 'index.html':
        print('PROCESSING FILE: ' + str(fn))
        fn_ascii = unicodedata.normalize('NFD', fn).encode('ascii', 'ignore')
        fn_ascii = fn_ascii.decode('ascii')
        m = re.search(submission_re, fn_ascii, re.UNICODE)
        stu_name = m.group(2).replace(' ', '_')
        script_name = m.group(8)
        stu_dir = args.odir + '/' + stu_name
        if not os.path.exists(stu_dir):
            os.makedirs(stu_dir)
        new_script_file = stu_dir + '/' + script_name
        shutil.copy(os.path.join(args.idir, fn), stu_dir + '/' + script_name)

