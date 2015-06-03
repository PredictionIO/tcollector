#!/usr/bin/env python

def enabled():
  return False

def urls():
  """Return a dictionary of metric names and URLs to check for latency"""
  return {'http.eventserver': 'http://localhost:7070'}
