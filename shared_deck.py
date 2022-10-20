import pandas as pd


class SharedDeck:
    def __init__(self, content_file_path):
        self.content_file_path = content_file_path
        self.content = pd.read_excel(content_file_path)

    def get_links(self) -> list:
        return list(self.content['front-image'])

    def save_content(self) -> None:
        self.content.to_excel(self.content_file_path, index=False)

    def generate_cards_with_image_on_front_side(self) -> list:
        cards = []
        for i in range(len(self.content)):
            back_translation, back_transcription = self.content['back-text-eng'][i].split('\n')
            card = {'front': f'<div class="center-flex"><img src="{self.content["link"][i]}"></div>',
                    'frontPreview': f'<div class="center-flex"><img src="{self.content["link"][i]}"></div>',
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
                    'backPreview': f'{back_translation} \n {back_transcription}',
                    'dateToRepeat': '',
                    'previousDateToRepeat': '',
                    'isWaitingToRepeat': True,
                    'repetitionCount': 0}
            cards.append(card)
        return cards

