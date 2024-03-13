import pandas as pd
import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(10000))  # 读取前10000字节来猜测编码方式
    return result['encoding']


file_paths = ['ks-projects-201801.csv', 'PoliceKillingsUS.csv']

for file_path in file_paths:
    encoding = detect_encoding(file_path)
    print(f"File: {file_path}, Encoding: {encoding}")
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            data = pd.read_csv(f)
    except UnicodeDecodeError:
        print("UnicodeDecodeError encountered. Trying with 'replace' error handling.")
        with open(file_path, 'r', encoding=encoding, errors='replace') as f:
            data = pd.read_csv(f)
    print(data.head())
