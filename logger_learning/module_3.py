import logging
from typing import Union

logger = logging.getLogger(__name__)


def square_number(number: Union[int, float]):

    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')

    return number**2
