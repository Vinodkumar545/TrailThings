import Logging.loghere as logger


def execute():

    def do_something():
        logger.log_info("do something")

    def debug(a, b):
        global c
        try:
            logger.log_info("To perform division")
            c = a/b
            logger.log_info(c)
            logger.log_info("Division performed")
        except Exception as e:
            logger.log_error("Class log_setup | debug () | Exp Desc:")
            logger.log_error(e)

    do_something()

    debug(10, 0)
    debug(10, 1)


if __name__ == '__main__':
    execute()
