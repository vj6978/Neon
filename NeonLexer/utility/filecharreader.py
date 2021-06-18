def fileCharReader(source):
    with open(source) as inp_file:
        print(source)
        for line in inp_file:
            for char in line:
                yield char