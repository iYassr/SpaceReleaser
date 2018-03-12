# SpaceReleaser
     ____                       ____      _                          
    / ___| _ __   __ _  ___ ___|  _ \ ___| | ___  __ _ ___  ___ _ __ 
    \___ \| '_ \ / _` |/ __/ _ \ |_) / _ \ |/ _ \/ _` / __|/ _ \ '__|
     ___) | |_) | (_| | (_|  __/  _ <  __/ |  __/ (_| \__ \  __/ |   
    |____/| .__/ \__,_|\___\___|_| \_\___|_|\___|\__,_|___/\___|_|   
          |_|                                               by iYassr

# SpaceReleaser
to find the largest files in your drive and delete them upon request <br />


## Getting Started
Please, follow the instructions below for installing and run SpeaceReleaser.

### Pre-requisites
Make sure you have installed the following tools:
```
Python 2.6 or later.
```

### Installing
```bash
$ git clone https://github.com/iYassr/SpaceReleaser.git
$ cd SpeaceReleaser
```

### Running
```bash
$ python3 SpaceReleaser.py -h
```


## Usage
usage: SpaceReleaser.py [-h] [-p path] [-d file index] [-t number of files] [-f] <br />                        

```
 -h, --help            show this help message and exit
  -p path, --path path  provide path to search into
  -d file index, --delete file index
                        index of the file to be deleted
  -t number of files, --top number of files
                        how many files to display
  -f, --full            to display the full path of the file
```

### Examples
```bash
$ python SpaceReleaser.py c:\users\x\desktop -f -d 11


             
 
