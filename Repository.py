import file_handeling
from Commit import Commit


#Initialization a new project
class Repository:
    def __init__(self, path):
        self.current_directory = path
        self.wit_path = file_handeling.join_path(self.current_directory, '.wit')
        self.stagin_area_path = file_handeling.join_path(self.wit_path, 'stagin_area')
        self.project_path = file_handeling.join_path(self.current_directory, 'current_version')
        self.commits_path = file_handeling.join_path(self.wit_path, 'commits')
        self.all_commits_json = file_handeling.join_path(self.wit_path, 'all_commits.json')

    def wit_init(self):
        #create .wit folder
        file_handeling.create_new_folder_in_the_selected_location(self.wit_path)

        #change .wit folder to hidden folder
        file_handeling.change_directory_to_hidden(self.wit_path)

        #create current version of project folder
        file_handeling.create_new_folder_in_the_selected_location(self.project_path)

        #create commits folder
        file_handeling.create_new_folder_in_the_selected_location(self.commits_path)

        # create stagin_area folder
        file_handeling.create_new_folder_in_the_selected_location(self.stagin_area_path)

        #create history commits file
        file_handeling.create_new_file_in_folder(self.all_commits_json)

    def wit_add(self, name_file):
        file_path = file_handeling.join_path(self.project_path, name_file)
        if file_handeling.check_if_path_of_file_exists(file_path):
            file_handeling.copy_file_to_folder(file_path, self.stagin_area_path)
        else:
            print(f"File {name_file} does not exist")

    def update_json_file(self, new_commit):
        dict_commit = {
            new_commit.id: (str(new_commit.date), new_commit.message)
        }
        file_handeling.write_json_to_file(self.all_commits_json, dict_commit)

    def wit_commit(self, message):
        new_commit = Commit(message)
        self.update_json_file(new_commit)
        new_commit_folder = file_handeling.join_path(self.commits_path, str(new_commit.id))
        file_handeling.copy_content_of_folder_to_other_folder(self.project_path, new_commit_folder)
        file_handeling.copy_content_of_folder_to_other_folder(self.stagin_area_path, new_commit_folder)
        file_handeling.delete_content_of_folder(self.stagin_area_path)

    def wit_status(self):
        content_stagin_area = file_handeling.get_all_files_in_selected_location(self.stagin_area_path)
        if len(content_stagin_area) != 0:
            print('There are files in stagin area - You have to do commit')

    def wit_log(self):
        content_file_json = file_handeling.get_content_json_file(self.all_commits_json)
        for key, value in content_file_json.items():
            print(f'{key}: {value}')

    def wit_checkout(self, id_of_commit):
        print("Insert your message for current commit")
        self.wit_commit(input())
        file_handeling.delete_content_of_folder(self.project_path)
        choice_version = file_handeling.join_path(self.commits_path, str(id_of_commit))
        file_handeling.copy_content_of_folder_to_other_folder(choice_version, self.project_path)
