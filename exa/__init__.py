# -*- coding: utf-8 -*-
# Copyright (c) 2015-2017, Exa Analytics Development Team
# Distributed under the terms of the Apache License 2.0
"""
Core features of the Exa data science framework. Full documentation available
at https://exa-analytics.github.io/exa/. The following is a short description.

- :mod:`~exa._version`: Version information
- :mod:`~exa.mpl`: Matplotlib wrappers
- :mod:`~exa.tex`: Text manipulation utilities

- :mod:`~exa.single`: Singleton metaclass
- :mod:`~exa.typed`: Strongly typed metaclass

- :mod:`~exa.base`: Abstract base classes
- :mod:`~exa.editor`: Base editors
- :mod:`~exa.container`: Frame container
- :mod:`~exa.data`: Frame data

- :mod:`exa.units`: Physical units
- :mod:`exa.constants`: Physical constants
- :mod:`exa.isotopes`: Chemical isotopes

Note:
    Static data is stored in the ``_static`` directory.
"""
def _jupyter_nbextension_paths():
    """
    Automatically generated by the `cookiecutter`_.

    .. _cookiecutter: https://github.com/jupyter/widget-cookiecutter
    """
    return [{
        'section': "notebook",
        'src': "../build/widgets",
        'dest': "jupyter-exa",
        'require': "jupyter-exa/extension"
    }]


from ._version import __version__
from . import mpl, tex
from .editor import Editor, Sections, Section
from .container import FrameContainer
from .data import FrameData
