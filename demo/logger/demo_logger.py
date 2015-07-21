import logging

my_logger = logging.getLogger('graylogger')


def log_debug(message, **kwargs):
    my_adapter = logging.LoggerAdapter(my_logger, kwargs)
    my_adapter.debug(message)

def log_info(message, **kwargs):
    my_adapter = logging.LoggerAdapter(my_logger, kwargs)
    my_adapter.info(message)

def log_warning(message, **kwargs):
    my_adapter = logging.LoggerAdapter(my_logger, kwargs)
    my_adapter.warning(message)

def log_error(message, **kwargs):
    my_adapter = logging.LoggerAdapter(my_logger, kwargs)
    my_adapter.error(message)