import logging

logging.basicConfig(filename="D:\Soft\Python_Selenium\Browser\est.log",
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                    )

logging.debug("This is a debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error('This is error message ')
logging.critical("This is Critical message")