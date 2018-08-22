import os


PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = open(os.path.join(PROJECT_HOME, 'VERSION')).read().strip()

CLI_CONTEXT_SETTINGS = dict(
    auto_envvar_prefix='aws_lookup',
    help_option_names=['-h', '--help', '?']
)
