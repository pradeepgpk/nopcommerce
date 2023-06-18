
# import logging
# def test_logDemo():
#
import inspect
import logging

class LogGen:
    @staticmethod
    def loggen():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(".//Logs//automation.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

