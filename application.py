import click
import logging.config
from datetime import datetime

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("shell_sort")

fh = logging.FileHandler('log/{:%Y-%m-%d-%H:%M:%S}.log'.format(datetime.now()))
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


@click.command()
@click.option('--array', prompt='Please enter array to sort(Comma separated, without spaces. Example: 3,7,1,5)',
              help='Array to sort')
def main(array):
    """
    This application sorting array using Shell method.
    """
    array = array.split(',')
    logger.info('Sorting data...')
    logger.info(shell_sort(array))
    logger.info('Exiting...')


def shell_sort(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


if __name__ == '__main__':
    main()
