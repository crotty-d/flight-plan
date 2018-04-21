# -*- coding: utf-8 -*-

"""Console script for flight_plan."""

import click


@click.command()
def main(args=None):
    """Console script for flight_plan."""
    click.echo("Replace this message by putting your code into "
               "flight_plan.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
