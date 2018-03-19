#encoding UTF-8

import pytest

pytest_plugins = "pytester"

def assert_outcomes(result, 
    passed=0, skipped=0, failed=0, error=0, xpassed=0, xfailed=0):
    
    outcomes = result.parseoutcomes()
    assert outcomes.get("passed", 0) == passed
    assert outcomes.get("skipped", 0) == skipped
    assert outcomes.get("failed", 0) == failed
    assert outcomes.get("error", 0) == error
    assert outcomes.get("xpassed", 0) == xpassed
    assert outcomes.get("xfailed", 0) == xfailed

def test_redmine_disabled(testdir):
    testdir.makepyfile('''
        import pytest
        @pytest.mark.redmine_issue(123)
        def test_pass():
            assert True
    ''')
    result = testdir.runpytest()
    assert_outcomes(result, passed=1)
