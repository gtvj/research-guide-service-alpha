from get_fragments import *
import json

with open('./app/data/references_in_guides_backlinked_deduped.json') as guides:
    guides = json.load(guides)


def get_guides_for_lettercode(lettercode, guides):
    if lettercode:
        if lettercode in guides:
            if 'guides' in guides[lettercode]:
                return guides[lettercode]['guides']
    return ''


def get_guides_for_series(lettercode, series, guides):
    if lettercode in guides:
        if series in guides[lettercode]['records']:
            if 'guides' in guides[lettercode]['records'][series]:
                return guides[lettercode]['records'][series]['guides']
    return ''


def get_guides_for_reference(lettercode, series, reference, guides):
    if lettercode in guides:
        if series in guides[lettercode]['records']:
            if 'records' in guides[lettercode]['records'][series]:
                if reference in guides[lettercode]['records'][series]['records']:
                    if 'guides' in guides[lettercode]['records'][series]['records'][reference]:
                        return guides[lettercode]['records'][series]['records'][reference]['guides']

    return ''


def get_guides(reference, guides):
    fragments = get_fragments(reference)

    letter_code = fragments['letter_code']
    series = fragments['series']
    reference = fragments['reference']

    results = {
        reference: get_guides_for_reference(letter_code, series, reference, guides),
        letter_code: get_guides_for_lettercode(letter_code, guides)
    }

    if series:
        results[series] = get_guides_for_series(letter_code, series, guides)

    return results
