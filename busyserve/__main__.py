""" API Server for Busylight for Humans™
"""

import typer
import uvicorn

from loguru import logger

cli = typer.Typer()


@cli.command()
def serve_busylight_api(
    debug: bool = typer.Option(False, "--debug", "-D", is_flag=True),
    host: str = typer.Option(
        "0.0.0.0", "--host", "-h", help="Host name to bind the server to."
    ),
    port: int = typer.Option(
        8192, "--port", "-p", help="Network port number to listen on."
    ),
) -> None:
    """ """

    (logger.enable if debug else logger.disable)("busyserve")
    logger.info("Busyserve For Humans™")


if __name__ == "__main__":
    exit(cli(name="busyserve"))
