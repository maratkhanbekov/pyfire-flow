import pandas as pd


class SharedDecks:
    def __init__(self, content_file_path):
        self.content_file_path = content_file_path
        self.content = pd.read_excel(content_file_path)

    def get_links(self) -> list:
        return list(self.content['front-image'])

    def save_storage_links(self, links) -> None:
        self.content['storage_links'] = links
        self.content.to_excel(self.content_file_path, index=False)

    def generate_cards_with_image_on_front_side(self) -> list:
        cards = []
        # for i in range(len(self.content)):
        for i in range(2):
            back_translation, back_transcription = self.content['back-text-eng'][i].split('\n')
            card = {'front': f'<div class="center-flex"><img src="{self.content["storage_links"][i]}"></div>',
                    'frontPreview': f'',
                    'back': f'''<div class="center-flex">
                                <div>
                                <h1>{back_translation}</h1>
                                </div>
                                <p></p>
                                <div>
                                <i>{back_transcription}</i>
                                </div>
                                </div>
                            ''',
                    'backPreview': f'{back_translation}',
                    'dateToRepeat': '',
                    'previousDateToRepeat': '',
                    'isWaitingToRepeat': True,
                    'repetitionCount': 0}
            cards.append(card)
        return cards

