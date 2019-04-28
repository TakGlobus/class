# Code/Directory

 test.py  
  python test.py --plot-figure --fit-curve  neuron  
 --> `http://neuralensemble.org/docs/PyNN/examples/simple_STDP.html`  

 Result  
 png output result after run test.py


# Tips for install
1. Conda-Env. e.g. conda create -n pynn python=3.6
2. Build pyNN from pip install  pip install pyNN
3. Build neuron from conda (bioconda)   https://anaconda.org/conda-forge/neuron)
4. conda install mpi4py, scipy and other modules
5. NERON with a miniconda installation,  
   conda install -c anaconda ncurses  
   nrnivmodl -loadflags "-L/path/to/miniconda/lib" at "~/miniconda3/envs/py3/lib/python3.6/site-packages/pyNN/neuron/nmodl"
