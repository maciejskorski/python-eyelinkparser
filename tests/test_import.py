

def test_package_imports():
    try:
        from python_eyelinkparser.eyelinkparser import parse, defaulttraceprocessor
    except:
        assert False
