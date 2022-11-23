from app.utils import msg


@task
def check_databases():
    logger = get_run_logger()
    logger.info(msg())


@flow(timeout_seconds=600)
def check_databases_flow():
    return check_databases()


if __name__ == "__main__":
    check_databases_flow()