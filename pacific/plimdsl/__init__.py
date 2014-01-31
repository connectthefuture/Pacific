import functools

from plim.adapters.pyramid_renderer import add_plim_renderer
from plim.lexer import compile_plim_source
from plim.lexer import STANDARD_PARSERS

from .parsers import PLIMDSL_PARSERS


PACIFIC_PARSERS = []
PACIFIC_PARSERS.extend(PLIMDSL_PARSERS)
PACIFIC_PARSERS.extend(STANDARD_PARSERS)
PACIFIC_PARSERS = tuple(PACIFIC_PARSERS)


preprocessor = functools.partial(compile_plim_source, parsers=PACIFIC_PARSERS)


def includeme(config):
    """
    Set up standard configurator registrations. Use via:

    .. code-block:: python

        config = Configurator()
        config.include('pyramid_mako')

    Once this function has been invoked, the ``.plim`` renderer
    is available for use in Pyramid. This can be overridden and more may be
    added via the ``config.add_plim_renderer`` directive.
    """
    config.add_directive('add_plim_renderer', add_plim_renderer)
    config.add_plim_renderer('.plim', preprocessor='pacific.plimdsl.preprocessor')