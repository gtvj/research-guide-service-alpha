from get_content_for_guides import *
import json


def test_get_content_for_guide():
    result = get_content_for_guide('british-army-officers-up-to-1913-further-research')

    expected = {
        "guide_href": "http://www.nationalarchives.gov.uk/help-with-your-research/research-guides/british-army-officers-up-to-1913-further-research/",
        "name": "British Army officers up to 1913: further research",
        "summary": [
            "This guide covers both: commissioned officers officers who were promoted through the ranks You might find it useful to read the blog Isaac Chetham: From \u2018Scum of the Earth\u2019 to Commissioned Officer in Wellington\u2019s Army which explains the process of researching an Officer in this period.",
            "Selected birth, marriage and death certificates for British Army officers (1755-1908) Browse: WO 32/8903-8920 (1777-1868) for baptismal certificates for British Army officers WO 42 (1755-1908) for certificates of marriage, birth of children, death and burial There are index books in the reading rooms at The National Archives at Kew to identify relevant records.",
            "The supporting documents often contain statements of service, certificates of baptism and letters of recommendation HO 51 (1758-1855) for military entry books WO 103 (1809, 1871-1914) for original submissions and entry books of submissions to the Sovereign of recommendations for staff and senior appointments, and for commissions and appointments Use the index IND 1/8914 to locate records of commissions in SP 44/164 (1679-1782)."
        ],
        "bigrams": [
            [
                [
                    "Army",
                    "officers"
                ],
                7
            ],
            [
                [
                    "British",
                    "Army"
                ],
                11
            ],
            [
                [
                    "WO",
                    "25"
                ],
                5
            ],
            [
                [
                    "half",
                    "pay"
                ],
                6
            ]
        ],
        "references": [
            "WO25",
            "WO25",
            "WO25",
            "PMG3",
            "PMG14",
            "PMG4",
            "PMG4",
            "WO24",
            "WO23",
            "WO61",
            "WO42",
            "WO32",
            "WO42",
            "WO25",
            "WO25",
            "WO31",
            "HO51",
            "WO103",
            "IND1",
            "SP44",
            "WO4",
            "WO74"
        ],
        "trigrams": [
            [
                [
                    "Army",
                    "officers",
                    "1913"
                ],
                3
            ],
            [
                [
                    "British",
                    "Army",
                    "officers"
                ],
                7
            ],
            [
                [
                    "certificates",
                    "British",
                    "Army"
                ],
                3
            ]
        ],
        "id": "british-army-officers-up-to-1913-further-research"
    }

    assert result == expected


def test_get_content_for_guide_which_does_not_exist():
    result = get_content_for_guide('this-guide-is-nonexistent')

    expected = None

    assert result == expected


def test_get_content_for_multiple_guides():
    list_of_guides = [
        'british-army-officers-up-to-1913-further-research',
        'searching-for-records-using-discovery'
    ]
    result = get_content_for_multiple_guides(list_of_guides)

    expected = [
        {
            "guide_href": "http://www.nationalarchives.gov.uk/help-with-your-research/research-guides/british-army-officers-up-to-1913-further-research/",
            "name": "British Army officers up to 1913: further research",
            "summary": [
                "This guide covers both: commissioned officers officers who were promoted through the ranks You might find it useful to read the blog Isaac Chetham: From \u2018Scum of the Earth\u2019 to Commissioned Officer in Wellington\u2019s Army which explains the process of researching an Officer in this period.",
                "Selected birth, marriage and death certificates for British Army officers (1755-1908) Browse: WO 32/8903-8920 (1777-1868) for baptismal certificates for British Army officers WO 42 (1755-1908) for certificates of marriage, birth of children, death and burial There are index books in the reading rooms at The National Archives at Kew to identify relevant records.",
                "The supporting documents often contain statements of service, certificates of baptism and letters of recommendation HO 51 (1758-1855) for military entry books WO 103 (1809, 1871-1914) for original submissions and entry books of submissions to the Sovereign of recommendations for staff and senior appointments, and for commissions and appointments Use the index IND 1/8914 to locate records of commissions in SP 44/164 (1679-1782)."
            ],
            "bigrams": [
                [
                    [
                        "Army",
                        "officers"
                    ],
                    7
                ],
                [
                    [
                        "British",
                        "Army"
                    ],
                    11
                ],
                [
                    [
                        "WO",
                        "25"
                    ],
                    5
                ],
                [
                    [
                        "half",
                        "pay"
                    ],
                    6
                ]
            ],
            "references": [
                "WO25",
                "WO25",
                "WO25",
                "PMG3",
                "PMG14",
                "PMG4",
                "PMG4",
                "WO24",
                "WO23",
                "WO61",
                "WO42",
                "WO32",
                "WO42",
                "WO25",
                "WO25",
                "WO31",
                "HO51",
                "WO103",
                "IND1",
                "SP44",
                "WO4",
                "WO74"
            ],
            "trigrams": [
                [
                    [
                        "Army",
                        "officers",
                        "1913"
                    ],
                    3
                ],
                [
                    [
                        "British",
                        "Army",
                        "officers"
                    ],
                    7
                ],
                [
                    [
                        "certificates",
                        "British",
                        "Army"
                    ],
                    3
                ]
            ],
            "id": "british-army-officers-up-to-1913-further-research"
        },
        {
            "guide_href": "http://www.nationalarchives.gov.uk/help-with-your-research/discovery-help/searching-for-records-using-discovery/",
            "name": "Searching for records using Discovery",
            "summary": [
                "Advanced search gives you the option to: use combinations of key words find an exact phrase exclude\u00a0certain words (for instance if you want to search for the name Austen but not to get results for Jane Austen) You can opt to search records that are held at: The National Archives other archives both Options on the Records tab The records tab has the following fields that you can complete to focus your search: Search Find words There are three sets of search boxes in this section: All of these words: searches for results that match all of the words you have entered into the search box.",
                "This tab features the following fields to help you focus your search: Search Find words All of these words: searches for record creators whose name or locations contain all of the words you have entered into the search box.",
                "This is same as putting quotation marks (\u201d \u201c) around a set of words Any of these words: searches for record creators whose name or location contain either one or more of the words you have entered into the search box."
            ],
            "bigrams": [
                [
                    [
                        "Any",
                        "words"
                    ],
                    4
                ],
                [
                    [
                        "For",
                        "example"
                    ],
                    4
                ],
                [
                    [
                        "National",
                        "Archives"
                    ],
                    16
                ],
                [
                    [
                        "This",
                        "inserting"
                    ],
                    6
                ],
                [
                    [
                        "box",
                        "This"
                    ],
                    6
                ],
                [
                    [
                        "entered",
                        "box"
                    ],
                    6
                ],
                [
                    [
                        "family",
                        "name"
                    ],
                    4
                ],
                [
                    [
                        "get",
                        "results"
                    ],
                    4
                ],
                [
                    [
                        "government",
                        "department"
                    ],
                    4
                ],
                [
                    [
                        "held",
                        "National"
                    ],
                    5
                ],
                [
                    [
                        "record",
                        "creator"
                    ],
                    5
                ],
                [
                    [
                        "record",
                        "creators"
                    ],
                    6
                ],
                [
                    [
                        "words",
                        "Any"
                    ],
                    4
                ],
                [
                    [
                        "words",
                        "entered"
                    ],
                    4
                ],
                [
                    [
                        "words",
                        "es"
                    ],
                    4
                ]
            ],
            "references": [
                "WO95"
            ],
            "trigrams": [
                [
                    [
                        "National",
                        "Archives",
                        "archives"
                    ],
                    3
                ],
                [
                    [
                        "box",
                        "This",
                        "inserting"
                    ],
                    4
                ],
                [
                    [
                        "creators",
                        "whose",
                        "name"
                    ],
                    3
                ],
                [
                    [
                        "entered",
                        "box",
                        "This"
                    ],
                    6
                ],
                [
                    [
                        "es",
                        "record",
                        "creators"
                    ],
                    3
                ],
                [
                    [
                        "es",
                        "results",
                        "match"
                    ],
                    3
                ],
                [
                    [
                        "held",
                        "National",
                        "Archives"
                    ],
                    5
                ],
                [
                    [
                        "record",
                        "creators",
                        "whose"
                    ],
                    3
                ],
                [
                    [
                        "words",
                        "Any",
                        "words"
                    ],
                    4
                ],
                [
                    [
                        "words",
                        "entered",
                        "box"
                    ],
                    4
                ]
            ],
            "id": "searching-for-records-using-discovery"
        }
    ]

    assert result == expected


def test_get_content_for_multiple_guides_including_non_existent():
    list_of_guides = [
        'british-army-officers-up-to-1913-further-research',
        'searching-for-records-using-discovery',
        'this-guide-does-not-exist'
    ]

    result = get_content_for_multiple_guides(list_of_guides)

    expected = [
        {
            "guide_href": "http://www.nationalarchives.gov.uk/help-with-your-research/research-guides/british-army-officers-up-to-1913-further-research/",
            "name": "British Army officers up to 1913: further research",
            "summary": [
                "This guide covers both: commissioned officers officers who were promoted through the ranks You might find it useful to read the blog Isaac Chetham: From \u2018Scum of the Earth\u2019 to Commissioned Officer in Wellington\u2019s Army which explains the process of researching an Officer in this period.",
                "Selected birth, marriage and death certificates for British Army officers (1755-1908) Browse: WO 32/8903-8920 (1777-1868) for baptismal certificates for British Army officers WO 42 (1755-1908) for certificates of marriage, birth of children, death and burial There are index books in the reading rooms at The National Archives at Kew to identify relevant records.",
                "The supporting documents often contain statements of service, certificates of baptism and letters of recommendation HO 51 (1758-1855) for military entry books WO 103 (1809, 1871-1914) for original submissions and entry books of submissions to the Sovereign of recommendations for staff and senior appointments, and for commissions and appointments Use the index IND 1/8914 to locate records of commissions in SP 44/164 (1679-1782)."
            ],
            "bigrams": [
                [
                    [
                        "Army",
                        "officers"
                    ],
                    7
                ],
                [
                    [
                        "British",
                        "Army"
                    ],
                    11
                ],
                [
                    [
                        "WO",
                        "25"
                    ],
                    5
                ],
                [
                    [
                        "half",
                        "pay"
                    ],
                    6
                ]
            ],
            "references": [
                "WO25",
                "WO25",
                "WO25",
                "PMG3",
                "PMG14",
                "PMG4",
                "PMG4",
                "WO24",
                "WO23",
                "WO61",
                "WO42",
                "WO32",
                "WO42",
                "WO25",
                "WO25",
                "WO31",
                "HO51",
                "WO103",
                "IND1",
                "SP44",
                "WO4",
                "WO74"
            ],
            "trigrams": [
                [
                    [
                        "Army",
                        "officers",
                        "1913"
                    ],
                    3
                ],
                [
                    [
                        "British",
                        "Army",
                        "officers"
                    ],
                    7
                ],
                [
                    [
                        "certificates",
                        "British",
                        "Army"
                    ],
                    3
                ]
            ],
            "id": "british-army-officers-up-to-1913-further-research"
        },
        {
            "guide_href": "http://www.nationalarchives.gov.uk/help-with-your-research/discovery-help/searching-for-records-using-discovery/",
            "name": "Searching for records using Discovery",
            "summary": [
                "Advanced search gives you the option to: use combinations of key words find an exact phrase exclude\u00a0certain words (for instance if you want to search for the name Austen but not to get results for Jane Austen) You can opt to search records that are held at: The National Archives other archives both Options on the Records tab The records tab has the following fields that you can complete to focus your search: Search Find words There are three sets of search boxes in this section: All of these words: searches for results that match all of the words you have entered into the search box.",
                "This tab features the following fields to help you focus your search: Search Find words All of these words: searches for record creators whose name or locations contain all of the words you have entered into the search box.",
                "This is same as putting quotation marks (\u201d \u201c) around a set of words Any of these words: searches for record creators whose name or location contain either one or more of the words you have entered into the search box."
            ],
            "bigrams": [
                [
                    [
                        "Any",
                        "words"
                    ],
                    4
                ],
                [
                    [
                        "For",
                        "example"
                    ],
                    4
                ],
                [
                    [
                        "National",
                        "Archives"
                    ],
                    16
                ],
                [
                    [
                        "This",
                        "inserting"
                    ],
                    6
                ],
                [
                    [
                        "box",
                        "This"
                    ],
                    6
                ],
                [
                    [
                        "entered",
                        "box"
                    ],
                    6
                ],
                [
                    [
                        "family",
                        "name"
                    ],
                    4
                ],
                [
                    [
                        "get",
                        "results"
                    ],
                    4
                ],
                [
                    [
                        "government",
                        "department"
                    ],
                    4
                ],
                [
                    [
                        "held",
                        "National"
                    ],
                    5
                ],
                [
                    [
                        "record",
                        "creator"
                    ],
                    5
                ],
                [
                    [
                        "record",
                        "creators"
                    ],
                    6
                ],
                [
                    [
                        "words",
                        "Any"
                    ],
                    4
                ],
                [
                    [
                        "words",
                        "entered"
                    ],
                    4
                ],
                [
                    [
                        "words",
                        "es"
                    ],
                    4
                ]
            ],
            "references": [
                "WO95"
            ],
            "trigrams": [
                [
                    [
                        "National",
                        "Archives",
                        "archives"
                    ],
                    3
                ],
                [
                    [
                        "box",
                        "This",
                        "inserting"
                    ],
                    4
                ],
                [
                    [
                        "creators",
                        "whose",
                        "name"
                    ],
                    3
                ],
                [
                    [
                        "entered",
                        "box",
                        "This"
                    ],
                    6
                ],
                [
                    [
                        "es",
                        "record",
                        "creators"
                    ],
                    3
                ],
                [
                    [
                        "es",
                        "results",
                        "match"
                    ],
                    3
                ],
                [
                    [
                        "held",
                        "National",
                        "Archives"
                    ],
                    5
                ],
                [
                    [
                        "record",
                        "creators",
                        "whose"
                    ],
                    3
                ],
                [
                    [
                        "words",
                        "Any",
                        "words"
                    ],
                    4
                ],
                [
                    [
                        "words",
                        "entered",
                        "box"
                    ],
                    4
                ]
            ],
            "id": "searching-for-records-using-discovery"
        }
    ]

    assert result == expected
