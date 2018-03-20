# encoding UTF-8

import pytest

import logging
LOG = logging.getLogger()

from redminelib import Redmine


class RedmineHooks:

    def __init__(self, connection, end_status):
        self.issues = dict()
        self.connection = connection
        self.end_status = end_status
    
    def add_issue_to_cache(self, issue):
        self.issues[issue.id] = issue
    
    def get_issue_info(self, issue_id):
        issue = self.connection.issue.get(issue_id)
    
    def pytest_collection_modifyitems(self, session, config, items):
        [item for item in items if item.get_marker('redmine_issue')]


def pytest_addoption(parser):
    group = parser.getgroup('Redmine Integration')

    group.addoption('--redmine', action='store_true', 
        dest='redmine', default=False,
        help='Enable Redmine plugin')

    group.addoption('--redmine-end-status', action='store', 
        dest='redmine-end-status', default=2,
        help='Redmine projects')
    
    group.addoption('--redmine-username', action='store', 
        dest='redmine-username', default='admin',
        help='Redmine username')

    group.addoption('--redmine-password', action='store', 
        dest='redmine-password', default='admin',
        help='Redmine password')

    group.addoption('--redmine-url', action='store', 
        dest='redmine-url', default='http://redmine',
        help='Redmine URL')


def pytest_configure(config):
    if config.getoption('redmine'):
        print('run with redmine plugin')
    
        connection = Redmine(
            url = config.getvalue('redmine-url'),
            username = config.getvalue('redmine-username'),
            password = config.getvalue('redmine-password')
        )

        redmine_plugin = RedmineHooks(
            connection,
            config.getoption('redmine-end-status')
        )

        assert config.pluginmanager.register(redmine_plugin, 'redmine-plugin')

