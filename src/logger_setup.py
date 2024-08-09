import logging
import os


def logger_setup(base, name):
    logger = logging.getLogger(f'{name}_{base}')
    logger.setLevel(logging.DEBUG)
    log_dir = os.path.join('logs', f'{name}_{base}')
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f'{base}.log')
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    csv_file = os.path.join(log_dir, f'{base}.csv')
    logger.csv_file = csv_file

    return logger
