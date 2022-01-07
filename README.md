# promQL to CSV
A tool to extract data from a Prometheus server trough promQL query to CSV

# Getting started
## Clone the repository
```bash
git clone https://github.com/daviddetorres/promql2csv
```

## Prerequisites
Install dependencies:
```
pip install -r requirements.txt
```

## Using the tool
Quick start: 
```
./promql2csv.py -q "up{job='prometheus'}"
```

Command line options:
```
usage: promql2csv.py [-h] [-o OUTPUT] [-u URL] [-p PORT] -q QUERY [-t TIME]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file [env var: OUTPUT]
  -u URL, --url URL     Prometheus server URL [env var: URL]
  -p PORT, --port PORT  Prometheus server port [env var: PORT]
  -q QUERY, --query QUERY
                        PromQL query [env var: QUERY]
  -t TIME, --time TIME  Seconds to query [env var: TIME]

  Defaults:
    --output:          output.csv
    --url:             localhost
    --port:            9090
    --time:            60

 If an arg is specified in more than one place, then commandline values override environment
variables which override defaults.
```

## Set up a local server
Prometheus server: 
```
docker run -d -p 9090:9090 prom/prometheus
```
