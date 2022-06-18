from {{cookiecutter.package_name}}.config import TaskConfig


def perform(config: TaskConfig):

    print(f"Task: {config.task} for {config.context}")
