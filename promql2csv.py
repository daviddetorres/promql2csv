#!/usr/bin/env python3
import configargparse
import logging

from extractor import extractor

VERSION = '0.0.1'

# Setup logger
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Setup command line arguments
parser = configargparse.ArgParser()

parser.add('-o',
          '--output',
          required=False,
          env_var='OUTPUT',
          default='output.csv',
          dest='output',
          help='Output file')

parser.add('-u',
          '--url',
          required=False,
          env_var='URL',
          default='localhost',
          dest='url',
          help='Prometheus server URL')

parser.add('-p',
          '--port',
          required=False,
          env_var='PORT',
          default='9090',
          dest='port',
          help='Prometheus server port')

parser.add('-q',
          '--query',
          required=True,
          env_var='QUERY',
          default='',
          dest='query',
          help='PromQL query')

parser.add('-t',
          '--time',
          required=False,
          env_var='TIME',
          default=60,
          dest='time',
          help='Seconds to query')

def main():
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        exit(1)
      
    logger.info('Starting promql2csv v{}'.format(VERSION))
    logger.debug('Arguments: \n{}'.format(parser.format_values()))
    extractor.extract(args, logger)
    logger.info('Finished')

if __name__ == '__main__':
    main()