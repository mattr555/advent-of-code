def filemap(func, filename, sep='\n'):
    with open(filename) as f:
        return list(map(func, f.read().strip().split(sep)))
