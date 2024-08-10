#!/usr/bin/env python3
import sys
from pyais import decode

k = 0
try:
    for line in iter(sys.stdin.readline, b''):
        k = k + 1
        aivdm_data_decoded = decode(line)
        print(aivdm_data_decoded)
except KeyboardInterrupt:
    sys.stdout.flush()
    pass
print(k)