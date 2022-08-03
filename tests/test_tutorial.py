from datamatrix import (
  operations as ops,
  functional as fnc,
  series as srs
)
from python_eyelinkparser.eyelinkparser import parse, defaulttraceprocessor

def test_tutorial():
    """Repeat the steps from https://pydatamatrix.eu/eyelinkparser/"""
    # The heavy lifting is done by eyelinkparser.parse()
    dm = parse(
        folder='src/python_eyelinkparser/data',           # Folder with .asc files
        traceprocessor=defaulttraceprocessor(
            blinkreconstruct=True, # Interpolate pupil size during blinks
            downsample=10,         # Reduce sampling rate to 100 Hz,
            mode='advanced'        # Use the new 'advanced' algorithm
        )
    )
    # To save memory, we keep only a subset of relevant columns.
    dm = dm[dm.set_size, dm.correct, dm.ptrace_sounds, dm.ptrace_retention, 
            dm.fixxlist_retention, dm.fixylist_retention]
    try:
        print(dm)
    except:
        assert False
