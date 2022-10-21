import os, path
import eng_to_ipa as p
import pandas as pd
import logging
from deep_translator import GoogleTranslator

def show_folder_structure(path_to_folder, path_from_content):
    for i in sorted(os.listdir(path_to_folder)):
        if not i.startswith('.'):
            print(path_from_content + i)


def get_name_of_files(path_to_folder, path_from_content):
    for i in sorted(os.listdir(path_to_folder)):
        if not i.startswith('.'):
            print(i.split('.')[0].title())


def get_name_of_files_without_numbers(path_to_folder, path_from_content):
    for i in sorted(os.listdir(path_to_folder)):
        if not i.startswith('.'):
            print(''.join([i for i in i.split('.')[0].title() if not i.isdigit()])[1:])

def translate_english_to_ipa(path_to_content, col):
    file = pd.read_excel(path_to_content)
    file['english-word-to-ipa'] = file[col].apply(lambda x: p.convert(x))
    file['back-text-eng'] = file[col] + '\n' + file['english-word-to-ipa']
    file.to_excel(path_to_content, index=False)
    logging.info(f'File {path_to_content} is updated.')


def translate_english_to_spanish(path_to_content, col):
    file = pd.read_excel(path_to_content)
    file['spanish-text'] = file[col].apply(lambda x: GoogleTranslator(source='auto', target='es').translate(x))
    file.to_excel(path_to_content, index=False)
    logging.info(f'File {path_to_content} is updated.')


if __name__ == '__main__':
    # City-life
    # show_folder_structure(path_to_folder = '../../shared-decks/media/city-life/city-file-svg-icons/', path_from_content='city-file-svg-icons/')
    # translate_english_to_ipa(path_to_content='../../shared-decks/media/city-life/content.xlsx', col='english-word')

    # Food
    # show_folder_structure(path_to_folder = '../../shared-decks/media/gastronomy/135541-gastronomy-set/svg', path_from_content='135541-gastronomy-set/svg/')
    # get_name_of_files(path_to_folder='../../shared-decks/media/gastronomy/135541-gastronomy-set/svg',
    #                       path_from_content='135541-gastronomy-set/svg/')
    # translate_english_to_ipa(path_to_content='../../shared-decks/media/gastronomy/content.xlsx', col='english-word')

    # Flags
    # show_folder_structure(path_to_folder = '../../shared-decks/media/flags/206589-international-flags/svg', path_from_content='206589-international-flags/svg/')
    # get_name_of_files_without_numbers(path_to_folder='../../shared-decks/media/flags/206589-international-flags/svg',
    #                   path_from_content='206589-international-flags/svg/')

    # world-landmarks
    # show_folder_structure(path_to_folder='../../shared-decks/media/world-landmarks/6406557-famous-landmarks/svg',
    #                       path_from_content='6406557-famous-landmarks/svg/')
    # get_name_of_files_without_numbers(path_to_folder='../../shared-decks/media/world-landmarks/6406557-famous-landmarks/svg',
    #                   path_from_content='world-landmarks/6406557-famous-landmarks/svg/')


    # music instruments
    # show_folder_structure(path_to_folder='../../shared-decks/media/music-instruments/836799-music-instruments/svg',
    #                       path_from_content='836799-music-instruments/svg/')
    # get_name_of_files_without_numbers(path_to_folder='../../shared-decks/media/music-instruments/836799-music-instruments/svg',
    #                   path_from_content='music-instruments/836799-music-instruments/svg/')

    translate_english_to_spanish('../../shared-decks/media/music-instruments/content.xlsx', col='english-word')