import logging
from typing import Union

logger = logging.getLogger(__name__)


def devide_number(dividend: Union[int, float], devider: Union[int, float]):

    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')

    try:
        return dividend / devider
    except ZeroDivisionError:
        logger.exception('Произошло деление на 0')