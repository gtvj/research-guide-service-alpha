import json

with open('./app/data/references_in_guides_backlinked_deduped.json') as guides:
    guides = json.load(guides)


def get_guides_for_lettercode(lettercode, guides):
    if (lettercode and guides[lettercode]):
        return guides[lettercode]
    return ''


def get_guides_for_series(lettercode, series, guides):
    lettercode_found = guides[lettercode] or False

    if (lettercode_found):
        series_found = guides[lettercode]["records"][series] or False

        if (series_found):
            return guides[lettercode]["records"][series]

    return ''


def get_guides_for_reference(lettercode, series, reference, guides):

    lettercode_found = guides[lettercode] or False

    if(lettercode_found):
        series_found = guides[lettercode]["records"][series] or False

        if(series_found):
            reference_found = guides[lettercode]["records"][series] or False

            if(reference_found):
                return guides[lettercode]["records"][series]["records"][reference]

    return ''
