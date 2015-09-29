assert True

try:
    assert False
except AssertionError:
    import sys
    print sys.exc_info()
    exit(1)
