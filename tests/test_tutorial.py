def test_get_tutorial():
    """Test the tutorial from https://pydatamatrix.eu/0.14/eyelinkparser/"""
    from datamatrix import (
    operations as ops,
    functional as fnc,
    series as srs
    )
    import pkg_resources 
    from importlib.resources import path
    import python_eyelinkparser
    from python_eyelinkparser.eyelinkparser import parse, defaulttraceprocessor

    def get_data(folder):
        # The heavy lifting is done by eyelinkparser.parse()
        dm = parse(
            folder=folder,           # Folder with .asc files
            traceprocessor=defaulttraceprocessor(
            blinkreconstruct=True, # Interpolate pupil size during blinks
            downsample=10,         # Reduce sampling rate to 100 Hz,
            mode='advanced'        # Use the new 'advanced' algorithm
            )
        )
        return dm
    
    folder = pkg_resources.resource_filename('python_eyelinkparser','data')
    _ = get_data(folder)


