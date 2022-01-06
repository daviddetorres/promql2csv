import time

APIError = Exception

def get_server_url(args):
  return 'http://{}:{}'.format(args.url, args.port)

def get_api_url(args):
  return '{}/api/v1/query_range'.format(get_server_url(args))

def get_query_range(args):
  return '{}?query={}&start={}&end={}&step={}'.format(get_api_url(args), args.query, int(time.time()) - args.time, int(time.time()), args.step)

def parse_result(result):
  if result['status'] == 'error':
    raise APIError(result['error'])
  return result['data']['result']

def extract(args, logger):
  logger.info('Extracting data from promQL query to CSV file')