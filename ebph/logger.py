import os, sys
import stat
import time
import gzip
import logging
from logging import handlers as handlers

from ebph.utils import read_chunks
from ebph import defs

class LoggerWriter:
    """
    LoggerWriter

    A helper class for redirecting stdout and stderr to loggers.
    """
    def __init__(self, level):
        self.level = level
        self.message = ""

    def write(self, message):
        """
        Write each line of the message to the log.
        """
        self.message = ''.join([self.message, message])
        if message.endswith('\n'):
            self.flush()

    def flush(self):
        """
        Provide a dummy flush method.
        """
        for line in self.message.split('\n'):
            if not line.strip():
                continue
            self.level(line)
        self.message = ""

class EBPHLoggerClass(logging.getLoggerClass()):
    """
    Custom logger class that allows for the logging of audit messages.
    """
    AUDIT = logging.WARN - 5
    SEQUENCE = logging.INFO - 5

    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)

        logging.addLevelName(EBPHLoggerClass.AUDIT, "AUDIT")
        logging.addLevelName(EBPHLoggerClass.SEQUENCE, "NEWSEQ")

    def audit(self, msg, *args, **kwargs):
        """
        Write a policy message to logs.
        This should be used to inform the user about policy decisions/enforcement.
        """
        if self.isEnabledFor(EBPHLoggerClass.AUDIT):
            self._log(EBPHLoggerClass.AUDIT, msg, args, **kwargs)

    def sequence(self, msg, *args, **kwargs):
        """
        Write a policy message to logs.
        This should be used to inform the user about policy decisions/enforcement.
        """
        if self.isEnabledFor(EBPHLoggerClass.SEQUENCE):
            self._log(EBPHLoggerClass.SEQUENCE, msg, args, **kwargs)

logging.setLoggerClass(EBPHLoggerClass)

class EBPHRotatingFileHandler(handlers.TimedRotatingFileHandler):
    """
    Rotates log files either when they have reached the specified
    time or when they have reached the specified size. Keeps
    backupCount many backups.

    This class uses camel casing because that's what the logging module uses.
    """
    def __init__(self, filename, maxBytes=0, backupCount=0, encoding=None,
            delay=0, when='h', interval=1, utc=False):
        handlers.TimedRotatingFileHandler.__init__(self, filename, when,
                interval, backupCount, encoding, delay, utc)
        self.maxBytes = maxBytes
        self.suffix = "%Y-%m-%d_%H-%M-%S"

        def rotator(source, dest):
            dest = f'{dest}.gz'
            try:
                os.unlink(dest)
            except FileNotFoundError:
                pass
            with open(source, 'r') as sf, gzip.open(dest ,'ab') as df:
                for chunk in read_chunks(sf):
                    df.write(chunk.encode('utf-8'))
            try:
                os.unlink(source)
            except FileNotFoundError:
                pass

        self.rotator=rotator

    def shouldRollover(self, record):
        """
        Overload shouldRollover method from base class.

        Does file exceed size limit or have we exceeded time limit?
        """
        if self.stream is None:
            self.stream = self._open()
        if self.maxBytes > 0:
            msg = f'{self.format(record)}\n'
            self.stream.seek(0, 2)
            if self.stream.tell() + len(msg) >= self.maxBytes:
                return 1
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        return 0

def setup_logger(args):
    # Make logfile parent directory
    os.makedirs(os.path.dirname(defs.LOGFILE), exist_ok=True)

    # Configure logging
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    formatter.datefmt = '%Y-%m-%d %H:%M:%S'

    logger = get_logger()
    if args.debug:
        logger.setLevel(logging.DEBUG)
    elif args.log_sequences:
        logger.setLevel(EBPHLoggerClass.SEQUENCE)
    else:
        logger.setLevel(logging.INFO)

    # Create and add handler
    if args.nolog:
        # Stream handler if we are writing to stdout
        handler = logging.StreamHandler()
    else:
        # Rotating handler if we are writing to log files
        # TODO: change this to allow configurable sizes, times, backup counts
        handler = EBPHRotatingFileHandler(
            defs.LOGFILE,
            maxBytes=(1024**3),
            backupCount=12,
            when='w0',
            interval=4
        )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # A little debug message to tell us the logger has started
    logger.debug('Logging initialized.')

def get_logger(name='ebph'):
    return logging.getLogger(name)
