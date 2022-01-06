def get_server_url(args):
  return 'http://{}:{}'.format(args.url, args.port)

def get_api_url(args):
  return '{}/api/v1/query_range'.format(get_server_url(args))

def extract(args, logger):
  logger.info('Extracting data from promQL query to CSV file')