#! python3
# TopSizeFiles.py - returns the largest file in a directory

import os.path
import operator
import argparse

parser = argparse.ArgumentParser(description="printing the largest files in your system")
parser.add_argument('-p', '-path', type=str, default='C:\\')
parser.add_argument('-d', '-delete', type=int)
parser.add_argument('-t', '-top', type=int, default=20)
parser.add_argument('-f', '-full', action='store_true', default=False)
args = parser.parse_args()


def to_mb(file_size):
    return '%d MB' % (file_size/100)


def delete_file(file_path):
    os.unlink(file_path)


def longest_string(list, top, full):
    maxstr = 0
    if full is True:
        for counter in range(top):
            if len(list[counter][0]) > maxstr:
                maxstr = len(list[counter][0])
    else:
        for counter in range(top):
            filenamelength = len(list[counter][0].split('\\')[-1])
            if filenamelength > maxstr:
                maxstr = filenamelength
    return maxstr


fileSizes = {}
try:
    for path, subFolders, files in os.walk(args.p):
        for fileName in files:

            fileSize = os.path.getsize(os.path.join(path, fileName))
            FileName = os.path.join(path, fileName)
            fileSizes[FileName] = fileSize
except Exception:
    pass
sorted_fileSizes = sorted(fileSizes.items(), key=operator.itemgetter(1))
sorted_fileSizes.reverse()
justing = longest_string(sorted_fileSizes, args.t, args.f)
for i in range(args.t):
    if args.f:
        fileName = sorted_fileSizes[i][0]
    else:
        fileName = sorted_fileSizes[i][0].split('\\')[-1]
    fileSize = to_mb(sorted_fileSizes[i][1])
    counter = '[%s]' % i
    print(counter.ljust(4), fileName.ljust(justing, '-'), fileSize)


if args.d is not None:
    print('do you want do delete %s? yes or no' % sorted_fileSizes[args.d][0])
    yesno = input()
    if str(yesno) == 'yes':
        delete_file(sorted_fileSizes[args.d][0])
        print(sorted_fileSizes[args.d][0] + ' Has been deleted')
    else:
        print('You chose no, exiting...')
        exit()
