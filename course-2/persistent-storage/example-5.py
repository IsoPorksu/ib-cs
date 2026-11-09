while True:
    try:
        file_name = input('Enter file name: ')
        with open(file_name, 'a') as f:
            print(440, file=f)
            break
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('Error:', e)