import re
import sys


def remove_dup(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    return result


with open('../main.tex') as f:
    data = f.read()  # read the entire document
    labels = re.findall(r'\\label{([^}.]*)}', data)  # look for the labels
    if len(set(labels)) != len(labels):  # check for duplicated labels
        print("Duplicated labels")
        sys.exit(1)
    # get the index of the labels
    labels = {k: i for i, k in enumerate(remove_dup(labels))}
    # get the references with \ref \cref and \Cref and split in case of multiple references
    refs = remove_dup([item for sublist in [x.split(',') for x in re.findall(r'\\C?c?ref{([^}.]*)}', data)] for item in sublist])
    for i, x in enumerate(refs[:-1]):
        for j, y in enumerate(refs[i+1:]):
            if x.split(":")[0] == y.split(":")[0] and labels[x] > labels[y]:
                print("Mismatch: {} {}".format(x, y))
