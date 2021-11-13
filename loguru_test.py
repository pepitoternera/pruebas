from loguru import logger


logger.remove()
logger.add('error.log', format="{time} {level} {message}", level="ERROR")


@logger.catch
def func(x, y):
    return 1/(x+y)


print(func(1, -1))
