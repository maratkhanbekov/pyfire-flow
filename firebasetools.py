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
        self.bucket_name = firebase_admin.storage.bucket().name
        self.bucket = self.storage_client.bucket(self.bucket_name)

        self.firedb = firebase_admin.firestore.client()

        logging.info(f"{self.__class__.__name__} successfully initialized")

    def upload_file(self, source_file_name, destination_blob_name, token) -> str:
        blob = self.bucket.blob(destination_blob_name)
        blob.metadata = {"firebaseStorageDownloadTokens": token}
        blob.upload_from_filename(source_file_name)
        logging.info(f"File {source_file_name} uploaded as {destination_blob_name} with token {token}.")

        end_point = 'https://firebasestorage.googleapis.com/v0/b'
        link = f'{end_point}/{self.bucket_name}/o/{destination_blob_name.replace("/", "%2F")}?alt=media&token={token}'

        return link

    def upload_data(self, data, destination_path) -> str:
        ref = self.firedb.collection(destination_path).document()
        data['uid'] = ref.id
        ref.set(data)
        logging.info(f"Data successfully uploaded to {destination_path} with UID: {ref.id}")
        return ref.id

    def delete_collections(self, path, batch_size):
        ref = self.firedb.collection(path)
        docs = ref.limit(batch_size).stream()
        deleted = 0

        for doc in docs:
            doc.reference.delete()
            deleted += 1
            logging.info(f'{doc.id} deleted.')

        if deleted >= batch_size:
            return self.delete_collections(path, batch_size)
