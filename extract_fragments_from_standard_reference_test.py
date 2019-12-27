from extract_fragments_from_standard_reference import *


def test_extract_fragments_from_standard_reference():

    simple_references = [
        {"reference": "ADM 104/140", "expected_letter_code": "ADM",
            "expected_series": "ADM 104"},
        {"reference": "AB ", "expected_letter_code": "AB", "expected_series": ""},
        {"reference": "AB", "expected_letter_code": "AB", "expected_series": ""}
    ]

    for example_ref in simple_references:

        result = extract_fragments_from_standard_reference(example_ref["reference"])

        assert result["letter_code"] == example_ref["expected_letter_code"]
        assert result["reference"] == example_ref["reference"]
        assert result["series"] == example_ref["expected_series"]
