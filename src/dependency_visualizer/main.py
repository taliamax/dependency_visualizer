import click


@click.command()
@click.version_option()
def main():
    click.echo('Hello, World!')


if __name__ == '__main__':  # pragma: no cover
    main()
