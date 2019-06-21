#!/usr/bin/env bash


COMMAND="cd build && rm -rf * && cmake .. && make && cd ../bin "
eval ${COMMAND}

COMMAND="./main"
#eval ${COMMAND}

COMMAND="cd ../src"
eval ${COMMAND}


python plot_samplers_comparisonPfree.py

python plot_samplers_convergenceSeries.py

python plot_samplers_convexS.py

python plot_samplers_convexP.py

python plot_samplers_convergenceNewton.py

python plot_samplers_functReconstr.py
