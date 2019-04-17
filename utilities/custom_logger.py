import logging
import inspect


def customLogger(loglevel=logging.DEBUG):

    # Gets the name of the class/method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

   ##fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='a')
    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(loglevel)
    formatter =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger



