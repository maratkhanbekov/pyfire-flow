from jsonschema import validate
from fireschemes import FlashcardsFirestoreSchemes
from firebasetools import FirebaseTools
from shared_deck import SharedDeck
import logging
import sys
from config import config


def upload_deck_media_files():
    path_from_current_folder_to_contents = '../../shared-decks/media/flags/'
    shared_decks = SharedDeck(content_file_path=f'{path_from_current_folder_to_contents}content.xlsx')
    destination_path = 'shared-decks/flags-v1/'

    firebase_tools = FirebaseTools(path_to_credentials='../flashcards-76b34-firebase-adminsdk-pnckt-daab1ad148.json',
                                   storage_bucket='flashcards-76b34.appspot.com')

    for i in range(len(shared_decks.content)):
        source_path_to_file = path_from_current_folder_to_contents + shared_decks.content['front-image'][i]
        filename = shared_decks.content['front-image'][i].split('/')[-1]
        link = firebase_tools.upload_file(source_file_name=source_path_to_file,
                                          destination_blob_name=destination_path + filename,
                                          token=config['shared-deck-content-token'])
        shared_decks.content.at[i, 'link'] = link
    shared_decks.save_content()


def upload_deck_content(destination_path, scale_mode=False):
    # Generate content
    path_from_current_folder_to_contents = '../../shared-decks/media/flags/'
    shared_deck = SharedDeck(content_file_path=f'{path_from_current_folder_to_contents}/content.xlsx')

    if not scale_mode:
        shared_deck.content = shared_deck.content.head(3)

    flashcards_firestore_schemes = FlashcardsFirestoreSchemes()
    deck_instance = flashcards_firestore_schemes.get_instance(key='deck')
    deck_instance['title'] = 'Learn Geography: World Flags'
    deck_instance['colorHex'] = flashcards_firestore_schemes.colors['Blues'][0]
    deck_instance['cards'] = shared_deck.generate_cards_with_image_on_front_side_simple(col_with_text='back-text-eng')

    # Upload the content
    validate(instance=deck_instance, schema=flashcards_firestore_schemes.schemes['deck'])
    logging.info("JSON instances are valid")

    firebase_tools = FirebaseTools(path_to_credentials='../flashcards-76b34-firebase-adminsdk-pnckt-daab1ad148.json',
                                   storage_bucket='flashcards-76b34.appspot.com')
    firebase_tools.upload_data(data=deck_instance, destination_path=destination_path)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    # upload_deck_media_files()
    # upload_deck_content('decks-user-ydj1i4cjKnVVJAMVGqDAPNLFqvD2', scale_mode=False)
    upload_deck_content('decks', scale_mode=False)


