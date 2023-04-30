import logging

def initLogObj():
    format_str = '%(ascTime)s:%(message)s'
    file_name = 'FORENSIC_LOG.log'
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    loggerObj = logging.getLogger('logger')
    return loggerObj