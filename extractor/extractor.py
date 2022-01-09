import time

APIError = Exception

def get_server_url(args):
  return 'http://{}:{}'.format(args.url, args.port)

def get_api_url(args):
  return '{}/api/v1/query_range'.format(get_server_url(args))

def get_query_range(args):
  return '{}?query={}&start={}&end={}&step={}s'.format(get_api_url(args), args.query, int(time.time()) - args.time, int(time.time()), args.step)

def parse_result(result):
  if result['status'] == 'error':
    raise APIError(result['error'])
  parsed_result = {}
  for series in result['data']['result']:
    key = str(series["metric"])
    parsed_result[key] = {str(value[0]): value[1] for value in series["values"]}
  return parsed_result

def create_rows(args, start_time, data):
  rows = []
  header = ['Timestamp']
  for key in data:
    header.append(key)
  rows.append(header)
  for timestamp in range(int(start_time), int(time.time()), int(args.step)):
    row = [str(timestamp)]
    for key in data:
      if str(timestamp) in data[key]:
        row.append(data[key][str(timestamp)])
      else:
        row.append('')
    rows.append(row)
  return rows

def extract(args, logger):
  logger.info('Extracting data from promQL query to CSV file')