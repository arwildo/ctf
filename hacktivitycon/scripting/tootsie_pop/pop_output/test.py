#!/usr/bin/python3
import filetype

def main():
    kind = filetype.guess('c40')
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)

if __name__ == '__main__':
    main()
