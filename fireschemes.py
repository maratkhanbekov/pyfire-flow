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
        },
        'banner': {
            'deckUids': [],
            'imageUrl': '',
            'subtitle': '',
            'title': ''
        },
        'module': {
            'banners': [],
            'deckUids': [],
            'order': 0,
            'title': '',
            'uid': ''
        }
    }

    colors = {
        'Greens': ['CEE7D9', 'E7E7CE', 'CEE7CE'],
        'Purples': ['DCCEE7', 'E7CEE1'],
        'Oranges': ['F3CDB7'],
        'Yellows': ['F2E8CF', 'FFEBAD'],
        'Blues': ['C4E7FD', 'A1D7DE'],
        'Reds': ['FCC1C3']
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
            'repetitionCount': {'type': 'number'}
        }

        self.schemes['deck'] = {
            'type': 'object',
            'properties': {
                'colorHex': {'type': 'string'},
                'cards': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': self.schemes['card']
                    }
                },
                'premium': {'type': 'boolean'},
                'title': {'type': 'string'},
                'uid': {'type': 'string'}
            }
        }

        self.schemes['banner'] = {
                'deckUids': {
                    'type': 'array',
                    'items': {
                        'type': 'string'
                    }
                },
                'imageUrl': {'type': 'string'},
                'subtitle': {'type': 'string'},
                'title': {'type': 'string'}
        }

        self.schemes['module'] = {
            'type': 'object',
            'properties': {
                'banners': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': self.schemes['banner']
                    }
                },
                'deckUids': {
                    'type': 'array',
                    'items': {
                        'type': 'string'
                    }
                },
                'title': {'type': 'string'},
                'order': {'type': 'number'},
                'uid': {'type': 'string'}
            }
        }

    def get_scheme(self, key):
        return self.schemes[key]

    def get_instance(self, key):
        return self.instances[key].copy()
