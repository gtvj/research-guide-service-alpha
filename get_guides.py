from get_fragments import *
import json


def load_guide_data():
    with open('app/data/references_in_guides_backlinked_deduped.min.json') as guides:
        guides = json.load(guides)

    return guides


def get_guides_for_lettercode(lettercode):
    guides = load_guide_data()

    if lettercode:
        if lettercode in guides:
            if 'guides' in guides[lettercode]:
                return guides[lettercode]['guides']
    return ''


def get_guides_for_series(lettercode, series):
    guides = load_guide_data()

    if lettercode in guides:
        if series in guides[lettercode]['records']:
            if 'guides' in guides[lettercode]['records'][series]:
                return guides[lettercode]['records'][series]['guides']
    return ''


def get_guides_for_reference(lettercode, series, reference):
    guides = load_guide_data()

    if lettercode in guides:
        if series in guides[lettercode]['records']:
            if 'records' in guides[lettercode]['records'][series]:
                if reference in guides[lettercode]['records'][series]['records']:
                    if 'guides' in guides[lettercode]['records'][series]['records'][reference]:
                        return guides[lettercode]['records'][series]['records'][reference]['guides']

    return ''


def get_guides(reference):
    fragments = get_fragments(reference)

    letter_code = fragments['letter_code']
    series = fragments['series']
    reference = fragments['reference']

    results = {
        reference: get_guides_for_reference(letter_code, series, reference),
        letter_code: get_guides_for_lettercode(letter_code)
    }

    if series:
        results[series] = get_guides_for_series(letter_code, series)

    return results
