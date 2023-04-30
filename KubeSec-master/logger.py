import logging

def giveMeLoggingObject():
    format_str = '%(asctime)s %(message)s'
    file_name = 'FORENSICS_LOG.log'
    logging.basicConfig(format= format_str, filename =file_name, level = logging.INFO)
    loggerObj = logging.getLogger('tcpserver')
    return loggerObj