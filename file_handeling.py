import os
import subprocess
import shutil
import json


def create_new_folder_in_the_selected_location(path):
    os.makedirs(path, exist_ok=True)


def join_path(path, name_folder_or_file):
    return os.path.join(path, name_folder_or_file)


def change_directory_to_hidden(path_dir):
    subprocess.run(['attrib', '+h', path_dir])


def create_new_file_in_folder(path_file):
    open(path_file, 'w').close()


def copy_file_to_folder(path_file, path_folder):
    try:
        shutil.copy(path_file, path_folder)
    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")


def get_content_json_file(json_file_path):
    try:
        #If The file is empty. Return an empty dictionary
        if os.stat(json_file_path).st_size == 0:
            return {}
        with open(json_file_path, 'r', encoding='utf-8') as file:
            content_json = json.load(file)
        return content_json

    except FileNotFoundError:
        print("File not found. Check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_json_to_file(json_file_path, new_dict_commit):
    content_json = get_content_json_file(json_file_path)
    content_json.update(new_dict_commit)
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(content_json, f, indent=4)


def get_all_files_in_selected_location(path):
    content_folder = os.listdir(path)
    return content_folder


def copy_content_of_folder_to_other_folder(path_folder_src, path_folder_dest):
    try:
        shutil.copytree(path_folder_src, path_folder_dest, dirs_exist_ok=True)
    except shutil.SameFileError:
        print("Source and destination represent the same directory.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_content_of_folder(path_folder):
    try:
        if os.path.exists(path_folder):
            # over all items in the folder
            for item in os.listdir(path_folder):
                item_path = join_path(path_folder, item)
                # If the item is a directory, remove it recursively
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    # If the item is a file, remove it
                    os.remove(item_path)
        else:
            print(f"The folder '{path_folder}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_if_path_of_file_exists(path_file):
    if os.path.exists(path_file):
        return True
    else:
        return False
