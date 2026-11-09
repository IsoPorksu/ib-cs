def filter_file(filename_in, filename_out, cond):
    output = []
    try:
        with (open(filename_in, 'r') as f1, open(filename_out, 'w') as f2):
            lines = [line.strip() for line in f1.readlines()]
            for line in lines:
                try:
                    if cond(line):
                        output.append(line)
                except Exception: print("exc")
            for line in output:
                print(line, file=f2)

    except Exception as e:
        print(e)
        return
    

def odd(s): return int(s) % 2 == 1
filter_file('course-2/persistent-storage/data/random_ints.txt', 'course-2/persistent-storage/data/odds.txt', odd)
