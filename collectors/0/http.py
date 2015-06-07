#!/usr/bin/env python

import sys
import time

try:
  import requests
except ImportError:
  requests = None

COLLECTION_INTERVAL=15

from collectors.lib import utils
from collectors.etc import httpconf

def collect():
  """Collects HTTP latencies in milliseconds from a list of ports in configuration"""
  ts = time.time()
  try:
    for metric, url in httpconf.urls().iteritems():
      response = requests.get(url)
      latency = response.elapsed.total_seconds() * 1000
      print("%s %i %f" % (metric, ts, latency))
  except Exception as e:
    utils.err("error: something wrong happened in http: %s" % e)

def main(args):
  """Collects HTTP latency"""

  if not httpconf.enabled():
    utils.err("info: http disabled")
    return 13

  if requests is None:
    utils.err("error: Python module 'requests' is missing")
    return 13

  while True:
    collect()
    sys.stdout.flush()
    time.sleep(COLLECTION_INTERVAL)

if __name__ == "__main__":
  sys.stdin.close()
  sys.exit(main(sys.argv))
