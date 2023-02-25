import os, sys
import secrets

# https://docs.github.com/en/actions/learn-github-actions/variables
# similar : https://github.com/saadmk11/github-action-utils


ACTION_ENV_DELIMITER: str = "__ENV_DELIMITER__"
COMMAND_MARKER: str = "::"

CACHE_FILE = "request_cache"


def _clean_markdown_string(markdown_string: str) -> str:
    """
    Removes `%25, %0D, %0A` characters from a string.

    :param markdown_string: string with markdown content
    :returns: string after escaping
    """
    return (
        str(markdown_string)
        .replace("%25", "%")
        .replace("%0D", "\r")
        .replace("%0A", "\n")
    )


class GithubConfigs:

    def __init__(self):
        self.repository = os.environ["GITHUB_REPOSITORY"]
        self.api_url = os.environ["GITHUB_API_URL"]
        self.summary_file = os.environ["GITHUB_STEP_SUMMARY"]
        self.env_variables_file = os.environ["GITHUB_ENV"]
        return

    def get_env_variables(self):
        environment_variable_dict = {}
        marker = f"<<{ACTION_ENV_DELIMITER}"

        with open(os.environ["GITHUB_ENV"], "rb") as file:
            for line in file:
                decoded_line: str = line.decode("utf-8")

                if marker in decoded_line:
                    name, *_ = decoded_line.strip().split("<<")

                    try:
                        decoded_value = next(file).decode("utf-8").strip()
                    except StopIteration:
                        break
                environment_variable_dict[name] = decoded_value
        return environment_variable_dict
