class FlashcardsFirestoreSchemes:
    """ Purpose: storing db structure """

    schemes = {}
    instances = {
        'deck': {
            'colorHex': '',
            'cards': [],
            'premium': False,
            'title': '',
            'uid': ''
        }
    }

    def __init__(self):
        self.schemes['card'] = {
            'back': {'type': 'string'},
            'backPreview': {'type': 'string'},
            'front': {'type': 'string'},
            'frontPreview': {'type': 'string'},
            'dateToRepeat': {'type': 'string'},
            'isWaitingToRepeat': {'type': 'boolean'},
            'previousDateToRepeat': {'type': 'string'},
            'repetitionCount': {'type': 'number'},
            'uid': {'type': 'string'}
        }

        self.schemes['deck'] = {
            'type': 'object',
            'properties': {
                'colorHex': {'type': 'string'},
                'cards': {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": self.schemes['card']
                    }
                },
                'premium': {'type': 'boolean'},
                'title': {'type': 'string'},
                'uid': {'type': 'string'}
            }
        }

    def get_scheme(self, key):
        return self.schemes[key]

    def get_instance(self, key):
        return self.instances[key]
