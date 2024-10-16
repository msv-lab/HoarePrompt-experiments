import logging
from pathlib import Path


def logger_setup(directory: Path, base: str):
    logger = logging.getLogger(f'{base}')
    logger.setLevel(logging.DEBUG)
    log_dir = directory / f'{base}'
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / f'{base}.log'
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.log_dir = log_dir
    logger.csv_file = log_dir / f'{base}.csv'

    return logger
