from unittest import TestCase

from click.testing import CliRunner

from aws_lookup import cli as aws_lookup_cli

CMD_OPTS = ['--version', '-h,', '?,', '--help']


class CLITest(TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_cmd_help(self):
        for help_flag in ['--help', '?', '-h']:
            result = self.runner.invoke(aws_lookup_cli.cli, [help_flag])
            for opt in CMD_OPTS:
                self.assertIn(opt, result.output)
