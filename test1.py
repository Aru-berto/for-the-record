import os


def listfiles(path):
    files = []
    for dirName, subdirList, fileList in os.walk(path):
        dir = dirName.replace(path, "")
        files.append(dir)
        # for fname in fileList:
        #    files.append(os.path.join(dir, fname))
    return files


x = listfiles("01. Master Fabrication Orders")
y = listfiles("02. Master Document Control PDF")


files_only_in_x = set(x) - set(y)
files_only_in_y = set(y) - set(x)
files_only_in_either = set(x) ^ set(y)
files_in_both = set(x) & set(y)
all_files = set(x) | set(y)


docs = 0
for i in files_only_in_y:
    print(i)
    print()
    docs += 1

print(docs)
