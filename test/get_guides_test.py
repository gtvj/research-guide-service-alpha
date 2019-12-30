from get_guides import *

with open('./app/data/references_in_guides_backlinked_deduped.json') as guides:
    guides = json.load(guides)


def test_get_guides_for_letter_code():
    result = get_guides_for_lettercode('AB', guides)

    expected = {
        "guides": {
            "contaminated-land": "Contaminated land"
        },
        "records": {
            "AB 11": {
                "guides": {
                    "photographs": "Photographs"
                }
            },
            "AB 13": {
                "guides": {
                    "photographs": "Photographs"
                }
            },
            "AB 18": {
                "guides": {
                    "photographs": "Photographs"
                }
            },
            "AB 5": {
                "guides": {
                    "architectural-drawings": "Architectural drawings"
                }
            },
            "AB 7": {
                "guides": {
                    "photographs": "Photographs"
                }
            }
        }
    }

    assert result == expected


def test_get_guides_for_series():
    result = get_guides_for_series('AB', 'AB 11', guides)

    expected = {
        "guides": {
            "photographs": "Photographs"
        }
    }

    assert result == expected


def test_get_guides_for_reference():
    result = get_guides_for_reference('ACT', 'ACT 1', 'ACT 1/632', guides)

    expected = {
        "guides": {
            "companies-and-businesses": "Companies and businesses"
        }
    }

    assert result == expected
