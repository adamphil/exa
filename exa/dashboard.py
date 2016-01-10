# -*- coding: utf-8 -*-
'''
Dashboard
=======================
The workspace is a way to track and interact with different sets of
:class:`~exa.relational.Session` objects, which themselves that keep track of
user work. This includes :class:`~exa.relational.Program`s,
:class:`~exa.relational.Project`s, :class:`~exa.relational.Job`s,
:class:`~exa.relational.File`s, and :class:`~exa.relational.Container`s.
'''
from ipywidgets import DOMWidget
from traitlets import Unicode
from exa.relational import Session
from exa.relational import Container as DBContainer
from exa.container import Container


class Dashboard(DOMWidget):
    '''
    '''
    _view_module = Unicode('nbextensions/exa/static/js/exa.dashboard.widget', sync=True)
    _view_name = Unicode('DashboardView', sync=True)

    def list_sessions(self):
        '''
        Listing of user's sessions.
        '''
        return Session._get_all()

    def list_containers(self):
        '''
        '''
        return DBContainer._get_all()

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Dashboard\n{0}'.format(self.list_sessions())

Dashboard = Dashboard()
