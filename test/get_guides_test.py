from get_guides import *

def test_get_guides_for_letter_code():

    result = get_guides_for_lettercode('AB')

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