import os
import glob
from dask import dataframe as dd 


def main():
    src_base_dir = os.environ['SRC_BASE_DIR']
    tgt_base_dir = os.environ['TGT_BASE_DIR']
    src_file_names = sorted(glob.glob(f'{src_base_dir}/NYSE*.txt.gz'))
    tgt_file_names = [
        file.replace('txt', 'json').replace('nyse_data', 'nyse_json')
        for file in src_file_names
        ]

    print('File format conversion started')
    df = dd.read_csv(
        src_file_names,
        names=['ticker', 'trade_date', 'open_price', 'low_price',
            'high_price', 'close_price', 'volume'],
        blocksize=None
    )
    print('Data Frame is created and will be written in JSON format')
    df.to_json(
        tgt_file_names,
        orient='records',
        lines=True,
        compression='gzip'
)
    print('File format conversion completed')


if __name__ == '__main__':
    main()