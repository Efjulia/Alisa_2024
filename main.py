import logging



logger = logging.getLogger(name='hjbj')

logging.basicConfig(
    filename='example.log',
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    level=logging.DEBUG
)


def log_to_file():
    i = 0
    while i < 10:
        logger.warning(i)
        i += 1


if __name__ == '__main__':
    log_to_file()