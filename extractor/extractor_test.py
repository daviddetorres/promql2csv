import configargparse
import time
import pytest

import extractor

def test_server_url():
    args = configargparse.Namespace(url='localhost', port='9090')
    assert extractor.get_server_url(args) == 'http://{}:{}'.format(args.url, args.port)

def test_api_url():
    args = configargparse.Namespace(url='localhost', port='9090')
    assert extractor.get_api_url(args) == 'http://{}:{}/api/v1/query_range'.format(args.url, args.port)

def test_query_range():
    args = configargparse.Namespace(url='localhost', port='9090', query='test_query', time=60, step='1m')
    assert extractor.get_query_range(args) == 'http://{}:{}/api/v1/query_range?query={}&start={}&end={}&step={}'.format(args.url, args.port, args.query, int(time.time()) - args.time, int(time.time()), args.step)

def test_parse_result_error():
    result = {"status":"error","errorType":"bad_data","error":"bad_data: no series found in response"}
    with pytest.raises(extractor.APIError):
        extractor.parse_result(result)

def test_parse_result_success():
    result = {"status":"success","data":{"resultType":"matrix","result":[{"metric":{"__name__":"up","instance":"localhost:9090","job":"prometheus"},"values":[[1641510018,"1"]]}]}}
