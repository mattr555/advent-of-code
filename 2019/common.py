def filemap(func, filename):
    with open(filename) as f:
        return list(map(func, f.read().strip().split('\n')))
