from reference_parser import *


def get_fragments(ref):
    if is_legacy_subclass_series(ref):
        return extract_fragments_from_legacy_sub_class_series(ref)
    else:
        return extract_fragments_from_standard_reference(ref)


def extract_fragments_from_legacy_sub_class_series(reference):

    lettercode_match = re.match(r'^(\w*)(\s)?', reference)
    series_match = re.match(r'(\w+\s\d+\/\d+)', reference)

    return {
        "letter_code": lettercode_match.group(1) if lettercode_match else "",
        "series": series_match.group(0) if series_match else "",
        "reference": reference
    }


def extract_fragments_from_standard_reference(reference = False):
    lettercode_match = re.match(r'^(\w*)(\s)?', reference)
    series_match = re.match(r'(\w+\s\d+)', reference)

    return {
        "letter_code": lettercode_match.group(1) if lettercode_match else "",
        "series": series_match.group(0) if series_match else "",
        "reference": reference
    }