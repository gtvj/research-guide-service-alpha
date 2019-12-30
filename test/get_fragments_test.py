from get_fragments import * 

def test_get_fragments():

    simple_references = [
        { "reference": "ADM 104/140", "expected_letter_code": "ADM", "expected_series": "ADM 104"},
        { "reference": "AB ", "expected_letter_code": "AB", "expected_series": ""},
        {"reference": "CP 25/1/284/18", "expected_letter_code": "CP",
            "expected_series": "CP 25/1"},
        { "reference": "AB", "expected_letter_code": "AB", "expected_series": ""}
    ]

    for reference in simple_references: 

        fragments = get_fragments(reference["reference"])

        assert fragments["letter_code"] == reference["expected_letter_code"]
        assert fragments["series"] == reference["expected_series"]