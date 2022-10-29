from firebasetools import FirebaseTools, send_multicast_message
import logging
import sys
from datetime import datetime


def get_uids_and_data_to_update(source_data, current_date, log=False):
    uids_to_update = {}
    update_counter = 1
    for uid, decks in source_data.items():
        for idx_d, deck in enumerate(decks):
            for deck_attr in deck:
                if deck_attr == 'cards':
                    for idx_c, card in enumerate(deck[deck_attr]):
                        if datetime.strptime(card['dateToRepeat'], '%d.%m.%Y') <= current_date:
                            source_data[uid][idx_d]['cards'][idx_c]['isWaitingToRepeat'] = True
                            if uid not in uids_to_update:
                                uids_to_update[uid] = {}
                                uids_to_update[uid]['cards_to_repeat'] = 1
                            else:
                                uids_to_update[uid]['cards_to_repeat'] += 1
                            if log:
                                print(f'{update_counter}', f'user_id: {uid}', f'deck title: {deck["title"]}',
                                      f"card front: {card['front'][:10]}", f"date to repeat: {card['dateToRepeat']}")
                            update_counter += 1
    return uids_to_update, source_data


def update_decks_data(user_uids, refresh_data):
    # For every user
    for uid in user_uids.keys():
        # Get decks
        dict_user_decks = refresh_data[uid]
        # For every deck
        for dict_user_deck in dict_user_decks:
            # Update data
            firebase_tools.update_document_data(collection_name=f'decks-user-{uid}',
                                                document_name=f'{dict_user_deck["uid"]}',
                                                data_to_update=dict_user_deck)
    logging.info(f'{len(user_uids)} decks updated.')


def generate_text_message(user_data, user_data_with_tokens):
    for user_uid in user_data.keys():
        # Create message
        user_data[user_uid]['message'] = {'title': "Let's repeat your flashcards!"}
        if user_data[user_uid]['cards_to_repeat'] == 1:
            user_data[user_uid]['message']['body'] = f"You've got 1 card to repeat"
        else:
            user_data[user_uid]['message']['body'] = f"You've got {int(user_data[user_uid]['cards_to_repeat'])} cards to repeat"
        user_data[user_uid]['message']['fcm_ios_tokens'] = [user['fcm_ios_tokens'] for user in user_data_with_tokens if user['uid'] == user_uid][0]


def execute_push_sending(user_data):
    n_pushes_sent = 0
    n_pushes_doesnt_sent = 0
    for user_uid in user_data.keys():
        if len(user_data[user_uid]['message']['fcm_ios_tokens']) > 0:
            send_multicast_message(title=user_data[user_uid]['message']['title'],
                                   body=user_data[user_uid]['message']['body'],
                                   tokens=user_data[user_uid]['message']['fcm_ios_tokens'])
            n_pushes_sent += 1
        else:
            n_pushes_doesnt_sent += 1
            logging.warning(f'{user_uid} user doesnt have any fcm_ios_token.')

    logging.info(f'{n_pushes_sent} out of {n_pushes_sent + n_pushes_doesnt_sent} pushes sent.')


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    firebase_tools = FirebaseTools(path_to_credentials='../flashcards-76b34-firebase-adminsdk-pnckt-daab1ad148.json',
                                   storage_bucket='flashcards-76b34.appspot.com')

    # Get all users
    list_users: list = firebase_tools.get_documents_from_collection(collection_name='users')

    # Get decks
    dict_decks_of_users: dict = firebase_tools.get_documents_from_collections(collection_prefix='decks-user-',
                                                                              list_collections_uids=[user['uid'] for user in list_users])
    # Get artifacts for push and upload
    dict_push_users_data, dict_refreshed_data = get_uids_and_data_to_update(source_data=dict_decks_of_users,
                                                                            current_date=datetime.today())
    # Update data
    update_decks_data(dict_push_users_data, dict_refreshed_data)

    # Generate text for push message
    generate_text_message(dict_push_users_data, list_users)

    # Send pushes
    execute_push_sending(dict_push_users_data)

    # TODO: store communication history
    # TODO: get status of message receiving

