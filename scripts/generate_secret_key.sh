#!/bin/bash

python -c 'import random; import string; print("".join([random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)]))'
{"mode":"full","isActive":false}