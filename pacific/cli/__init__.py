"""
Manage Pacific Apps from a command line.

Usage:
    pacific <command> <config>
    pacific -h | --help

Options:
    -h, --help       Show this screen.
    -V, --version    Show version.

The most commonly used commands are:
    run    Run a project instance.

"""
from pkg_resources import get_distribution

from docopt import docopt
from pyramid.scripts import pserve


def main():
    """ Entry point for the ``pacific`` command.
    """
    args = docopt(__doc__, argv=None, help=True,
                  version=get_distribution('Pacific'),
                  options_first=False)

    return COMMANDS[args['<command>']](args)


def cmd_run(args):
    """

    :param dict args:
    :return:
    """
    pserve_argv = ['pserve', args['<config>']]
    return pserve.main(pserve_argv)


COMMANDS = {
    'run': cmd_run
}