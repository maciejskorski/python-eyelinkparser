from datamatrix import (
  operations as ops,
  functional as fnc,
  series as srs
)
from python_eyelinkparser.eyelinkparser import parse, defaulttraceprocessor


@fnc.memoize(persistent=True)
def get_data():

    # The heavy lifting is done by eyelinkparser.parse()
    dm = parse(
        folder='data',           # Folder with .asc files
        traceprocessor=defaulttraceprocessor(
          blinkreconstruct=True, # Interpolate pupil size during blinks
          downsample=10,         # Reduce sampling rate to 100 Hz,
          mode='advanced'        # Use the new 'advanced' algorithm
        )
    )
    # To save memory, we keep only a subset of relevant columns.
    dm = dm[dm.set_size, dm.correct, dm.ptrace_sounds, dm.ptrace_retention, 
            dm.fixxlist_retention, dm.fixylist_retention]
    return dm