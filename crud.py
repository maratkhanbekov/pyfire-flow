from firebasetools import FirebaseTools
import logging
import sys

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    firebase_tools = FirebaseTools(path_to_credentials='../flashcards-76b34-firebase-adminsdk-pnckt-daab1ad148.json',
                                   storage_bucket='flashcards-76b34.appspot.com')

    firebase_tools.delete_collections(path='decks', batch_size=100)