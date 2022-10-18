import firebase_admin
from firebase_admin import credentials, storage, db, firestore
from google.cloud import storage
from google.oauth2 import service_account
import logging


class FirebaseTools:
    def __init__(self, path_to_credentials, storage_bucket):
        firebase_admin.initialize_app(credentials.Certificate(path_to_credentials), {'storageBucket': storage_bucket})

        self.credentials = service_account.Credentials.from_service_account_file(path_to_credentials)
        self.storage_client = storage.Client(credentials=self.credentials)
        self.bucket = self.storage_client.bucket(firebase_admin.storage.bucket().name)

        self.firedb = firebase_admin.firestore.client()

        logging.info(f"{self.__class__.__name__} successfully initialized")

    def upload_file(self, source_file_name, destination_blob_name):
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        logging.info(f"File {source_file_name} uploaded to {destination_blob_name}.")

    def get_storage_link(self, link):
        return self.bucket.blob(link).public_url

    def get_storage_links(self, links):
        storage_links = []
        for link in links:
            storage_links.append(self.get_storage_link(link))
        return storage_links

    def upload_data(self, data, destination_path):
        ref = self.firedb.collection(destination_path).document()
        data['uid'] = ref.id
        ref.set(data)
        logging.info(f"Data successfully uploaded to {destination_path}.")
