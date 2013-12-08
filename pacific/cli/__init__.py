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
import configparser
from pkg_resources import get_distribution

import yaml
from docopt import docopt
from pyramid.scripts import pserve

from pacific.config import parse_db_settings


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
    yaml_config = args['<config>']
    with open(yaml_config, 'r') as configfile:
        pconf = yaml.load(configfile.read())

    ini_config = 'development.ini'
    conf = configparser.ConfigParser()
    conf.read(ini_config)

    conf['app:main']['pacific.superuser_id'] = str(pconf['superuser_id'])
    db_settings = parse_db_settings(pconf['db'])
    conf['app:main'].update(db_settings)

    compiled_config = '.{}.pconf'.format(yaml_config)
    with open(compiled_config, 'w') as configfile:
        conf.write(configfile)

    pserve_argv = ['pserve', compiled_config]
    return pserve.main(pserve_argv)


COMMANDS = {
    'run': cmd_run
}
