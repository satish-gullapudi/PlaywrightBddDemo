import logging

LOGGER_NAME = 'automation_logger'


def setup_logger(scenario_log_file):
    """
    Configures a logger for one scenario.
    Uses 'w' mode to REPLACE the log file if it already exists.

    Args:
        scenario_log_file (str): The unique path for the scenario log file.

    Returns:
        logging.Logger: The configured logger instance.
    """

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)

    # Clear existing handlers to prevent log duplication/mixing
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Define the formatter
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] (%(name)s) %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 1. Create File Handler (using 'w' mode to overwrite/replace)
    file_handler = logging.FileHandler(
        filename=scenario_log_file,
        mode='w'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 2. Create Console Handler (shared across scenarios for real-time view)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger