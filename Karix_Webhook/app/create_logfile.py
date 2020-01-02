def createLogfile():
    import logging
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler("logfile.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)