from statistics import fmean
import io, sys
from time import sleep

while True:
    try:
        file_name = input('Enter file name: ')
        with open(file_name, 'r') as f:
            lst = [float(line.strip()) for line in f.readlines()]
            print(int(fmean(lst)))
            break
    except FileNotFoundError:
        print('File not found.')
    except io.UnsupportedOperation:
        print('File not readable.')
    except PermissionError:
        print('Permission denied.')
    except ValueError:
        print('Value error: check the format of the numbers in the file - are they all valid decimal numbers? Are there even any numbers in there?')
        sleep(4)
        print('Are you sure it will work now? Have you fixed it?')
        sleep(4)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(f'Error (line {exc_tb.tb_lineno}):', e, )
        print(e.__class__.__name__)