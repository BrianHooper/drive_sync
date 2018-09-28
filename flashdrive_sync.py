#   pickle/depickle old file list
#   compare old file list to new file list
#   separate new files, modified files, and deleted files

def read_file(input_filename):
    read_data = {}
    with open(input_filename, 'r') as file:
        for line in file.read().splitlines():
            parsed_line = line.split(',')
            read_data[parsed_line[0]] = int(parsed_line[1])
    return read_data


def pickle_filelist(filelist):
    pass


def depickle_file_list(pickled_filename):
    pass


def find_new_files(current_files, old_files):
    new_files = []
    for x in current_files:
        if x not in old_files:
            new_files.append(x)
    return new_files


def find_modified_files(current_files, old_files):
    modified_files = []
    for x in current_files:
        if x in old_files and current_files[x] != old_files[x]:
            modified_files.append(x)
    return modified_files


def find_deleted_files(current_files, old_files):
    deleted_files = []
    for x in old_files:
        if x not in current_files:
            deleted_files.append(x)
    return deleted_files


drive1 = read_file("drive1.csv")
old = read_file("drive1.csv")
drive1["newfile.txt"] = 12345
drive1["file1.txt"] = 1234567
del drive1["file1.txt"]
new_files = find_deleted_files(drive1, old)
print(new_files)