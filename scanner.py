from pyzbar.pyzbar import decode
import cv2
import os
import argparse
import json
import sys
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_qr(image_path: str):
    image = cv2.imread(image_path)
    #print(type(image))
    codes = decode(image)
    decoded = []
    for code in codes:
        # (x, y, w, h) = code.rect
        codeData = code.data.decode("utf-8")
        # codeType = code.type
        # print("[INFO] Found {} with code: {}".format(codeType, codeData))
        # code_dict[str(codeData)] = [(x, y), (x + w, y + h)]
        decoded.append(str(codeData))

    return decoded

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to the input folder containing all the image to be processed", required = True)
    # parser.add_argument("--output", help="path to the output folder containing all output in the json format", required = True)
    args = parser.parse_args()
    # print('input param=', args.input)
    decoded = read_qr(args.input)
    print(json.dumps(decoded))
    sys.stdout.flush()
    # if not os.path.exists(args.output):
    #     os.mkdir(args.output)

    # files = os.listdir(args.input)
    # count = 0

    # for file in files:

    #     decoded = multiple_qr(image_path = os.path.join(args.input, file))
    #     print("Decoded=", decoded)
        # with open(os.path.join(args.output, file.split('.')[0]), 'w') as jsonfile:
        #     json.dump(decoded, jsonfile)
        # if len(decoded):
        #     count = count + 1 
        # print('-' * 50)
    
    # print(count)

if __name__ == '__main__':
    main()