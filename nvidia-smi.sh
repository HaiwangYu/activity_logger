#/bin/env bash

nvidia-smi -lms 250 --format=csv --query-gpu=utilization.gpu,memory.used
