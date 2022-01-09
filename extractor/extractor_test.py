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
    args = configargparse.Namespace(url='localhost', port='9090', query='test_query', time=60, step='1')
    assert extractor.get_query_range(args) == 'http://{}:{}/api/v1/query_range?query={}&start={}&end={}&step={}s'.format(args.url, args.port, args.query, int(time.time()) - args.time, int(time.time()), args.step)

def test_parse_result_error():
    result = {"status":"error","errorType":"bad_data","error":"bad_data: no series found in response"}
    with pytest.raises(extractor.APIError):
        extractor.parse_result(result)

def test_parse_result_success():
    result = {"status":"success","data":{"resultType":"matrix","result":[{"metric":{"__name__":"up","instance":"localhost:9090","job":"prometheus"},"values":[[1641510018,"1"]]}]}}
    expected_result = {
            "{\'__name__\': \'up\', \'instance\': \'localhost:9090\', \'job\': \'prometheus\'}": 
            {"1641510018": '1'}
        }
    
    assert extractor.parse_result(result) == expected_result

def test_create_rows():
    args = configargparse.Namespace(url='localhost', port='9090', query='test_query', time=60, step='60')
    start_time = str(int(time.time()) - args.time)
    data = {
            "{\'__name__\': \'up\', \'instance\': \'localhost:9090\', \'job\': \'prometheus\'}": 
            {start_time: '1'}
        }
    expected_result = [
            ['Timestamp', "{\'__name__\': \'up\', \'instance\': \'localhost:9090\', \'job\': \'prometheus\'}"],
            [start_time, '1']
    ]
    assert extractor.create_rows(args, int(start_time), data) == expected_result