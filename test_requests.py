#!/usr/bin/env python3
"""Minimal test: can the frozen app import requests?"""
import sys
import os

print("Python executable:", sys.executable)
print("sys.path:")
for p in sys.path[:5]:
    print(" ", p)

try:
    import requests
    print("requests OK:", requests.__version__)
except ImportError as e:
    print("FAILED to import requests:", e)
    sys.exit(1)

print("All good!")
