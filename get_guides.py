import json


with open('./app/data/references_in_guides_backlinked_deduped.json') as guides:
    guides = json.load(guides)

def get_guides_for_lettercode(letter_code):

    if(letter_code and guides[letter_code]):
        return guides[letter_code]