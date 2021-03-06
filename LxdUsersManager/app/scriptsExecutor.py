import subprocess
import os
import sys

scripts_path = sys.argv[1]


def run_script_with_args(script_name, params):
    path = os.path.join(os.getcwd(), scripts_path, script_name)
    return subprocess.check_output(["bash", path] + params)


def get_user_history(name):
    return run_script_with_args("getHistory.sh", [name])


def create_user(name, password):
    run_script_with_args("createUser.sh", [name, password])


def remove_user(name):
    run_script_with_args("removeUser.sh", [name])


def get_user_last_modified_file(name, path_to_repositories):
    return run_script_with_args("getLastChangedFile.sh", [path_to_repositories, name])
