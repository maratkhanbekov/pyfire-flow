from fireschemes import FlashcardsFirestoreSchemes
import logging
from jsonschema import validate
from firebasetools import FirebaseTools
import sys

def upload_first_layer(destination_path='modules'):
    flashcards_firestore_schemes = FlashcardsFirestoreSchemes()
    module_instance = flashcards_firestore_schemes.get_instance(key='module')

    # Flags
    banner_instance1 = flashcards_firestore_schemes.get_instance(key='banner')
    banner_instance1['title'] = 'Learn Geography: World Flags'
    banner_instance1['subtitle'] = 'Solid pack with 260 world flags'
    banner_instance1['imageUrl'] = 'https://firebasestorage.googleapis.com/v0/b/flashcards-76b34.appspot.com/o/system%2Fshared-deck%2Fworld_flags.pdf?alt=media&token=32b1f7a1-35c4-43b6-b96d-707f210e35c4'
    banner_instance1['deckUids'] = ['ryCxyNU70l7hSPvwzhgk']

    banner_instance2 = flashcards_firestore_schemes.get_instance(key='banner')
    banner_instance2['title'] = 'Learn Geography: Landmarks'
    banner_instance2['subtitle'] = 'We collected 60 prominent world landmarks inside'
    banner_instance2[
        'imageUrl'] = 'https://firebasestorage.googleapis.com/v0/b/flashcards-76b34.appspot.com/o/system%2Fshared-deck%2Flandmarks.pdf?alt=media&token=36ef9060-bc7b-4ce6-a340-3287cf27de97'
    banner_instance2['deckUids'] = ['7uYz0ANu04iGrR2CiX8Q']

    module_instance['title'] = 'Most popular'
    module_instance['order'] = 1
    module_instance['deckUids'] = ['ibEwupshkVzeHtwGgMvM', 'OubyMO68aPYk7ZuRuSOf']
    module_instance['banners'] = [banner_instance1, banner_instance2]

    validate(instance=module_instance, schema=flashcards_firestore_schemes.schemes['module'])
    logging.info("JSON instances are valid")

    firebase_tools = FirebaseTools(path_to_credentials='../flashcards-76b34-firebase-adminsdk-pnckt-daab1ad148.json',
                                   storage_bucket='flashcards-76b34.appspot.com')
    firebase_tools.upload_data(data=module_instance, destination_path=destination_path)


def upload_second_layer(destination_path='modules'):
    flashcards_firestore_schemes = FlashcardsFirestoreSchemes()
    module_instance = flashcards_firestore_schemes.get_instance(key='module')

    module_instance['title'] = 'Learn Spanish'
    module_instance['order'] = 2
    module_instance['deckUids'] = ['XsiSEaLtiXla4eGsXQwB', 'Lq8ExKGNGQs2EvqoR5q8']

    validate(instance=module_instance, schema=flashcards_firestore_schemes.schemes['module'])
    logging.info("JSON instances are valid")

    firebase_tools = FirebaseTools(path_to_credentials='../flashcards-76b34-firebase-adminsdk-pnckt-daab1ad148.json',
                                   storage_bucket='flashcards-76b34.appspot.com')
    firebase_tools.upload_data(data=module_instance, destination_path=destination_path)


def upload_third_layer(destination_path='modules'):
    flashcards_firestore_schemes = FlashcardsFirestoreSchemes()
    module_instance = flashcards_firestore_schemes.get_instance(key='module')

    banner_instance1 = flashcards_firestore_schemes.get_instance(key='banner')
    banner_instance1['title'] = 'Learn Chemistry: Periodic Elements'
    banner_instance1['subtitle'] = 'This deck will help you visualize and rememeber every chemical element'
    banner_instance1['imageUrl'] = 'https://firebasestorage.googleapis.com/v0/b/flashcards-76b34.appspot.com/o/system%2Fshared-deck%2Fperiodic_elements.pdf?alt=media&token=2a0a7c4c-f5a7-4671-bd2a-e2e3d8fdc9c4'
    banner_instance1['deckUids'] = ['XpWIZ6Wp0ANzmbVaf9nk']

    module_instance['title'] = 'Learn Science'
    module_instance['order'] = 3
    module_instance['banners'] = [banner_instance1]

    validate(instance=module_instance, schema=flashcards_firestore_schemes.schemes['module'])
    logging.info("JSON instances are valid")

    firebase_tools = FirebaseTools(path_to_credentials='../flashcards-76b34-firebase-adminsdk-pnckt-daab1ad148.json',
                                   storage_bucket='flashcards-76b34.appspot.com')
    firebase_tools.upload_data(data=module_instance, destination_path=destination_path)


def clean_modules():
    firebase_tools = FirebaseTools(path_to_credentials='../flashcards-76b34-firebase-adminsdk-pnckt-daab1ad148.json',
                                   storage_bucket='flashcards-76b34.appspot.com')
    firebase_tools.delete_collections(path='modules', batch_size=10)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    # clean_modules()
    upload_first_layer()
    # upload_second_layer()
    # upload_third_layer()
