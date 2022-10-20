from fireschemes import FlashcardsFirestoreSchemes


def upload_first_layer_without_banner():
    flashcards_firestore_schemes = FlashcardsFirestoreSchemes()
    module_instance = flashcards_firestore_schemes.get_instance(key='module')

    module_instance['title'] = 'The most popular decks'
    module_instance['order'] = '1'
    module_instance['deckUids'] = []

def upload_second_layer_without_folders():
    flashcards_firestore_schemes = FlashcardsFirestoreSchemes()
    banner_instance1 = flashcards_firestore_schemes.get_instance(key='banner')
    banner_instance1['title'] = ''
    banner_instance1['subtitle'] = ''
    banner_instance1['imageUrl'] = []
    banner_instance1['deckUids'] = []

    module_instance = flashcards_firestore_schemes.get_instance(key='module')

    module_instance['banners'] = [banner_instance1]
    module_instance['title'] = ''
    module_instance['order'] = ''
    module_instance['uid'] = ''
    module_instance['deckUids'] = ''

if __name__ == 'main':
    upload_first_layer_without_banner()




