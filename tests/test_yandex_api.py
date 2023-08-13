import requests
import pytest
import dotenv

import os


class TestFolderCreation:
    dotenv.load_dotenv()
    token = os.getenv('YANDEX_TOKEN')
    test_folder_name = 'test_folder'
    url = r'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
            'Accept': 'application/json',
            'Authorization': f"OAuth {token}"
        }

    def setup_method(self):
        if self.test_folder_name in self.get_folders_list():
            self.delete_test_folder()

    def teardown_method(self):
        self.delete_test_folder()

    def get_folders_list(self):
        response = requests.get(url=self.url, params={"path": r'/'}, headers=self.headers)
        folder_names = list()
        for item in response.json()['_embedded']['items']:
            if item['type'] == 'dir':
                folder_names.append(item['name'])
        return folder_names

    def delete_test_folder(self):
        requests.delete(url=self.url, params={"path": self.test_folder_name}, headers=self.headers)

    def create_test_folder(self):
        response = requests.put(url=self.url, params={"path": self.test_folder_name}, headers=self.headers)
        return response
    
    def test_creating_folder_status_code(self):
        response = self.create_test_folder()
        assert response.status_code == 201

    def test_creating_folder_dir_list(self):
        response = self.create_test_folder()
        assert self.test_folder_name in self.get_folders_list()

    def test_creating_exists_folder(self):
        response_1 = self.create_test_folder()
        response_2 = self.create_test_folder()
        assert response_2.status_code == 409