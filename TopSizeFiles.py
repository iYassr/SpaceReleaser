#! python3
# TopSizeFiles.py - returns the largest file in a directory


## # LIBRARIES # ##
import os.path
import operator
import argparse

## # MAIN FUNCTIONS # ##

def parse_args():
    parser = argparse.ArgumentParser(description="printing the largest files in your system")
    parser.add_argument('-p', '--path', type=str, default='C:\\', help='provide path to search into', metavar='path')
    parser.add_argument('-d', '--delete', type=int, help='index of the file to be deleted', metavar='file index')
    parser.add_argument('-t', '--top', type=int, default=20, help='how many files to display', metavar='number of files')
    parser.add_argument('-f', '--full', action='store_true', default=False, help='to display the full path of the file')
    return parser.parse_args()

def to_mb(file_size):
    return '{} MB'.format(file_size/1000000)


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

def banner():
    banner = """
     _____             _____ _ _        ____  _         
    |_   _|__  _ __   |  ___(_) | ___  / ___|(_)_______ 
      | |/ _ \| '_ \  | |_  | | |/ _ \ \___ \| |_  / _ \\
      | | (_) | |_) | |  _| | | |  __/  ___) | |/ /  __/
      |_|\___/| .__/  |_|   |_|_|\___| |____/|_/___\___|
              |_|           
              
                                             by Yasser                             
    """
    print(banner)


def main():
    banner()
    args = parse_args()

    fileSizes = {}
    try:
        for path, subFolders, files in os.walk(args.path):
            for fileName in files:

                fileSize = os.path.getsize(os.path.join(path, fileName))
                FileName = os.path.join(path, fileName)
                fileSizes[FileName] = fileSize
    except Exception:
        pass
    sorted_files = sorted(fileSizes.items(), key=operator.itemgetter(1))
    sorted_files.reverse()
    justing = longest_string(sorted_files, args.top, args.full)
    for i in range(args.top):
        if args.full:
            fileName = sorted_files[i][0]
        else:
            fileName = sorted_files[i][0].split('\\')[-1]
        fileSize = to_mb(sorted_files[i][1])
        counter = '[%s]' % i
        print(counter.ljust(4), fileName.ljust(justing, '-'), fileSize)


    if args.delete is not None:
        print('do you want do delete %s? yes or no' % sorted_files[args.delete][0])
        yesno = input()
        if str(yesno) == 'yes':
            delete_file(sorted_files[args.delete][0])
            print(sorted_files[args.delete][0] + ' Has been deleted')
        else:
            print('You chose no, exiting...')
            exit()

main()
