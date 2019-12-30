from extract_fragments_from_legacy_subclass_series import *


def test_extract_fragments_from_legacy_subsclass_series():

    legacy_subclass_series = [
        {"reference": "CP 25/1/284/18", "expected_letter_code": "CP",
            "expected_series": "CP 25/1"}
    ]

    for example_ref in legacy_subclass_series:

        result = extract_fragments_from_legacy_sub_class_series(example_ref["reference"])

        assert result["letter_code"] == example_ref["expected_letter_code"]
        assert result["reference"] == example_ref["reference"]
        assert result["series"] == example_ref["expected_series"]
