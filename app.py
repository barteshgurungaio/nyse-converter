import os
from dask import dataframe as dd 


def main():
    src_base_dir = os.environ['SRC_BASE_DIR']
    tgt_base_dir = os.environ['TGT_BASE_DIR']
    print('File format conversion started')
    df = dd.read_csv(
        f'{src_base_dir}/NYSE*.txt.gz',
        names=['ticker', 'trade_date', 'open_price', 'low_price',
            'high_price', 'close_price', 'volume'],
        blocksize=None
    )
    print('Data Frame is created and will be written in JSON format')
    df.to_json(
        f'{tgt_base_dir}/part-*.json.gz',
        orient='records',
        lines=True,
        compression='gzip',
        name_function=lambda i: '%05d' % i
)
    print('File format conversion completed')


if __name__ == '__main__':
    main()