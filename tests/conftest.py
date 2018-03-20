#encoding UTF-8

import pytest
from redminelib import Redmine

pytest_plugins = "pytester"

REDMINE_ARGS = [
    '--redmine',
    '--redmine-end-status', 'closed',
    '--redmine-url', 'http://localhost:3000',
    '--redmine-username', 'pytest',
    '--redmine-password', 'pytest_access'
]

def assert_outcomes(result, 
    passed=0, skipped=0, failed=0, error=0, xpassed=0, xfailed=0):
    
    outcomes = result.parseoutcomes()
    assert outcomes.get("passed", 0) == passed
    assert outcomes.get("skipped", 0) == skipped
    assert outcomes.get("failed", 0) == failed
    assert outcomes.get("error", 0) == error
    assert outcomes.get("xpassed", 0) == xpassed
    assert outcomes.get("xfailed", 0) == xfailed

@pytest.fixture(scope='session')
def redmine():
    conn = Redmine(url='http://localhost:3000', username='pytest', password='pytest_access')
    return conn

@pytest.fixture(scope='session')
def conftest_text():
    return '''
        import pytest 

        FAKE_ISSUES = {

            '1' : {
                'id' : 1,
                'status' : {
                    'id' : 1, 
                    'name' : 'new'
                }
            }
        }

        @pytest.mark.tryfirst
        def pytest_collection_modifyitems(session, config, items):
            plug = config.pluginmanager.getplugin('redmine-plugin')
            assert plug is not None
            
            for fake_issue in FAKE_ISSUES.values():
                plug.add_issue_to_cache(fake_issue)
    '''
