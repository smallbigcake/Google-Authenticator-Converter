import cv2
import sys
import os

from converter import Converter


def main(file_paths):

    if not check_file_path(file_paths):
        print('File not found.')
        sys.exit(-1)

    migration_list = get_str_from_qr_code(file_paths)
    plain_list = convert(migration_list)

    for each_plain in plain_list:
        print(each_plain)


def convert(migration_list):
    plain_list = []
    for migration in migration_list:
        converter = Converter()
        converter.from_migration_string(migration)
        each_plain_list = converter.to_plain_string()
        plain_list.extend(each_plain_list)

    return plain_list


def get_str_from_qr_code(file_paths):

    migration_list = []
    for each_file_path in file_paths:
        migration_str = read_qr_code(each_file_path)
        migration_list.append(migration_str)

    return migration_list


def read_qr_code(file_path):
    qr_file = cv2.imread(file_path)
    qr_detector = cv2.QRCodeDetector()
    result = qr_detector.detectAndDecode(qr_file)

    return result[0]


def check_file_path(file_path):
    for each_file_path in file_path:
        if not os.path.isfile(each_file_path):
            print(f'File not found: {each_file_path}')
            return False

    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python qrcode.py <filename1> [<filename2>] [<filename3>] ...')
        sys.exit(-1)

    print(sys.argv)
    main(sys.argv[1:])

