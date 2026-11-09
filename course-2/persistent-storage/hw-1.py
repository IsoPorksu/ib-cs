import pathlib, pickle

lst = []
for _ in range(10000):
    lst.append(4) # chosen by fair dice roll.
                  # guaranteed to be random.

file_path = pathlib.Path('course-2/persistent-storage/data') / 'random_ints.txt'

try:
    if file_path.exists():
        f = open(file_path, 'r')
        read_lst = [int(line) for line in f.read().splitlines()]
        f.close()
        print(read_lst)
    else:
        f = open(file_path, 'w')
        for i in lst:
            print(i, file=f)
        f.close()

except Exception as e: # handle any exception raised
    print('text file exception:', e)

file_path = pathlib.Path('course-2/persistent-storage/data') / 'random_ints.ser'

try:
    if file_path.exists():
        f = open(file_path, 'rb')
        read_lst = pickle.load(f)
        f.close()
        print(read_lst)
    else:
        f = open(file_path, 'wb')
        pickle.dump(lst, f)
        f.close()

except Exception as e: # handle any exception raised
    print('serialisation exception:', e)
