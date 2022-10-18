from jsonschema import validate

from fireschemes import FlashcardsFirestoreSchemes
from firebasetools import FirebaseTools
from shared_decks import SharedDecks
import logging
import sys


def example_pipeline(update_storage_links=False):

    # Get content file
    shared_decks = SharedDecks(content_file_path='./../shared-decks/media/animals/contents.xlsx')

    # Generate and save storage links
    firebase_tools = FirebaseTools(path_to_credentials='flashcards-76b34-firebase-adminsdk-pnckt-daab1ad148.json',
                                   storage_bucket='flashcards-76b34.appspot.com')

    if update_storage_links:
        local_links = shared_decks.get_links()
        storage_links = firebase_tools.get_storage_links(links=local_links)
        shared_decks.save_storage_links(storage_links)

    # Generate content to upload
    flashcards_firestore_schemes = FlashcardsFirestoreSchemes()
    deck_instance = flashcards_firestore_schemes.get_instance(key='deck')
    deck_instance['title'] = 'Learn english: Animals'
    deck_instance['colorHex'] = 'E7CEE1'
    deck_instance['cards'] = shared_decks.generate_cards_with_image_on_front_side()

    # Data validation
    validate(instance=deck_instance, schema=flashcards_firestore_schemes.schemes['deck'])
    logging.info("JSON instances are valid")

    # Upload the content
    firebase_tools.upload_data(data=deck_instance, destination_path='decks-user-Es31ehDRQcVITXAqMu0N8M38hi83')


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    example_pipeline()
