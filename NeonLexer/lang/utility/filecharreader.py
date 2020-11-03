def fileCharReader(src):
    with open(src) as inp_file:
        for line in inp_file:
            for char in line:
                yield char