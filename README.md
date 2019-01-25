# intersect-dirs
A tool to determine which files in folder A are not in folder B

## Example
Folder Structure:
```
.
├── dir_a
│   ├── file1.txt
│   ├── file2.txt
│   ├── file5 - Copy.txt
│   ├── file5.txt
│   └── Folder
│       └── file3.txt
└── dir_b
    ├── file1.txt
    ├── file2.txt
    └── file4.txt
```

Command:
```
python intersect_dirs.py dir_a dir_b
```

Output:
```json
{
    "8254c329a92850f6d539dd376f4816ee2764517da5e0235514af433164480d7a": [
        "dir_a\\file5 - Copy.txt",
        "dir_a\\file5.txt"
    ],
    "2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6": [
        "dir_a\\Folder\\file3.txt"
    ]
}
```
