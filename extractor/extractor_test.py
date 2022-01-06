import configargparse

import extractor

def test_server_url():
    args = configargparse.Namespace(url='localhost', port='9090')
    assert extractor.get_server_url(args) == 'http://{}:{}'.format(args.url, args.port)

def test_api_url():
    args = configargparse.Namespace(url='localhost', port='9090')
    assert extractor.get_api_url(args) == 'http://{}:{}/api/v1/query_range'.format(args.url, args.port)