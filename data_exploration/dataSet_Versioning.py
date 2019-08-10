import os
#import datetime
import re
#import pickle
import json

import  data_exploration.dataset as datasetmodule
from data_exploration.pachyderm_client import PachydermClient


class PachydermRepoManager:
    """
    Manages repos on pachyderm cluster
    """
    def __init__(self, list_of_repo: list):
        #self.logger = XprLogger()
        #self.config = XprConfigParser(config_path)["pachyderm"]
        self.list_of_repo = list_of_repo
        self.pachyderm_client = self.connect_to_pachyderm()


    def connect_to_pachyderm(self):
        """
        connects to pachyderm cluster and returns a PfsClient connection instance

        :return:
            returns a PfsClient Object
        """
        client = PachydermClient(
            "172.16.3.51","30650"
        )
        print(f'Client:{client}')
        #client.create_new_repo('test_abzooba_dvc_5')
        self.new_repo = client.create_new_repo('test_abzooba_dvc_3')
        print(f'Repo Created:\n{self.new_repo}')
        #self.list_of_repo=client.get_repo()
        #print(self.list_of_repo)


        return client


    def create_repo(self, repo_json):
        """
        creates a new repo on pachyderm cluster
        :param repo_json:
            Information of the repo to be created
        :return:
        """
        if "repo_name" not in repo_json:
            #raise RepoNotProvidedException()R
            raise Exception
        if not self.name_validity_check(repo_json["repo_name"]):
            #raise PachydermFieldsNameException()
            raise Exception
        description = ""
        if "description" in repo_json:
            description = repo_json["description"]

        print()
        self.pachyderm_client.create_new_repo(repo_json["repo_name"],
                                              description)
        return


    @staticmethod
    def name_validity_check(name):
        """
        Checks if the name provided contains only alphanumeric characters,
        underscore or dashes

        :param name:
            (str) : name
        :return:
            check status i.e. True or False
        """
        accepted_pattern = r"[\w, -]+$"
        if not isinstance(name, str):
            # raise PachydermFieldsNameException()
            raise Exception
        match = re.match(accepted_pattern, name)
        if not match:
            return False
        return True


    def delete_repo(self, repo_name):
        """
        deletes a repo from pachyderm cluster

        This is admin level operation
        :param repo_name:
            name of the repo to be deleted
        :return:
            no return statement
        """
        self.pachyderm_client.delete_repo(repo_name)

    # def creating_first_repo(self):
    #
    #     client.create_repo('test_Anushree')
    #     with client.commit('test_Anushree', 'master') as c:
    #      client.put_file_bytes(c, '/dir_a/data.txt', b'DATA')
    #     client.get_repo()
    #     return

        # with client.commit('test', 'master') as c:
        #     client.put_file_bytes(c, '/dir_a/data.txt', b'DATA')


    #def push_dataset(self, repo_name, branch_name, dataset, description):

    def push_dataset(self, dataset, description):
        """
        pushes a dataset into pachyderm cluster

        :param repo_name:
            name of the repo i.e. project in this case
        :param branch_name:
            name of the branch
        :param dataset:
            AbstractDataset object with info on dataset
        :param description:
            brief description regarding this push
        :return:
            returns commit_id if push is successful
        """
        print('Here')
        print('Hi'.format(dataset))
        abstract_dataset = datasetmodule.AbstractDataset
        if not isinstance(dataset, abstract_dataset):
            # raise DatasetInfoException("Provided dataset is invalid")
            raise Exception
        # First Save the dataset locally


    @staticmethod
    def fetch_file_list(dataset_dir, dataset_name):
        """
        fetches the list of file paths recursively in a directory

        :param dataset_dir:
            path of the dataset directory
        :param dataset_name:
            name of the dataset
        :return:
            returns a list of file paths inside the dataset directory
        """
        file_list = []
        pachyderm_destination_path = f"dataset/{dataset_name}"
        for dir_path, dirs, files in os.walk(dataset_dir):
            for file in files:
                file_path = os.path.join(dir_path, file)
                destination_path = file_path.replace(dataset_dir, pachyderm_destination_path, 1)
                file_list.append((file_path, destination_path))

        return file_list

if __name__ == "__main__":
    p = PachydermRepoManager(list_of_repo=list())

     # read file
    with open('create_repo.json', 'r') as myfile:
        data=myfile.read()

    # parse file
    obj = json.loads(data)# show values
    print("usd: " + str(obj['repo_name']))
    p.create_repo(obj)
    #p.delete_repo('test_repo2')
    #p = PachydermRepoManager()
    #p.connect_to_pachyderm()
    #p.create_repo()



    #print(p)
