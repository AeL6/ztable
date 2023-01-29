# open file for reading only
with open('./ztable.txt', 'r') as f:
    # go through each line
    for i in f.readlines():
        # format line by removing new line characters and store each column in an array
        _line = i.strip().split()

        # store row index
        _index = _line[0]

        # remove the row index from original line
        _line.pop(0)

        # turn each column values into actual floats to remove unnecessary ''
        _newline = list(map(float, _line))

        # format it to be a valid javascript array
        print(f"['{_index}', {_newline},],")
