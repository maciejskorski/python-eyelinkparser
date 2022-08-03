

def test_package_imports():
    """Test importing submodules"""
    try:
        from python_eyelinkparser import eyelinkparser, eyetribeparser, gazepointparser
    except:
        assert False
