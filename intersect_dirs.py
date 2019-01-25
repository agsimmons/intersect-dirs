import argparse
import hashlib
import json
import pathlib
import sys


BUFFERSIZE = 65536


def _parse_arguments():
    parser = argparse.ArgumentParser(description='Ensure that all files in dir A are in dir B')
    parser.add_argument('dir_a')
    parser.add_argument('dir_b')
    return parser.parse_args()


def _hash_file(path):
    file_hash = hashlib.sha256()
    with open(path, mode='rb') as f:
        buffer = f.read(BUFFERSIZE)
        while len(buffer) > 0:
            file_hash.update(buffer)
            buffer = f.read(BUFFERSIZE)

    return file_hash.hexdigest()


def _create_hash_dict(path):
    hash_dict = {}
    for file in [file for file in path.glob('**/*') if file.is_file()]:
        file_hash = _hash_file(file)
        if file_hash in hash_dict:
            hash_dict[file_hash].append(file)
        else:
            hash_dict[file_hash] = [file]

    return hash_dict


def intersect_dirs(src, dest):
    src_dict = _create_hash_dict(src)
    dest_dict = _create_hash_dict(dest)

    src_set = set(src_dict)
    dest_set = set(dest_dict)

    intersection_set = src_set - dest_set

    # Files in src that are not in dest
    intersection_dict = {}
    for file_hash in intersection_set:
        intersection_dict[file_hash] = src_dict[file_hash]

    return intersection_dict


def main():
    args = _parse_arguments()

    dir_a = pathlib.Path(args.dir_a)
    dir_b = pathlib.Path(args.dir_b)

    # Ensure both directories are valid
    if not dir_a.is_dir():
        print('Error: dir_a is not valid')
        sys.exit(1)
    if not dir_b.is_dir():
        print('Error: dir_b is not valid')
        sys.exit(1)

    intersection = intersect_dirs(dir_a, dir_b)

    # Convert paths to strings
    for file_hash in intersection.keys():
        intersection[file_hash] = list(map(str, intersection[file_hash]))

    print(json.dumps(intersection, indent=4))


if __name__ == '__main__':
    main()
