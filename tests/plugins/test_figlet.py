import logging
from doteki.plugins.figlet import run


def test_prototype():
    settings = {"ascii_text": "hola"} 
    expected = """ _           _       \n| |__   ___ | | __ _ \n| '_ \\ / _ \\| |/ _` |\n| | | | (_) | | (_| |\n|_| |_|\\___/|_|\\__,_|\n                     \n"""
    expected = "<pre style='background: none; border: none'>" + expected + "</pre>"
    result = run(settings)
    expected = expected.replace(" ", "S").replace("\n","r")
    result = result.replace(" ", "S").replace("\n","r")

    print(repr(expected))
    print(repr(result))
    assert result == expected


def test_proto_2():
    import pyfiglet
    
    expected = """ _           _       \n| |__   ___ | | __ _ \n| '_ \\ / _ \\| |/ _` |\n| | | | (_) | | (_| |\n|_| |_|\\___/|_|\\__,_|\n                     \n"""
    result = pyfiglet.figlet_format("hola")

    #expected = expected.replace(" ", "S").replace("\n","r")
    #result = result.replace(" ", "S").replace("\n","r")

    #print(repr(expected))
    #print(repr(result))
    assert result == expected

#If no parameters, result is none
#Test is superseeded by test_empty_text
"""def test_empty_settings(caplog):

    settings = {}
    
    with caplog.at_level(logging.ERROR):
        result = run(settings)
    assert result is None
    assert "No settings provided for the Figlet plugin" in caplog.text"""

#If no text, result is none

def test_empty_text(caplog):

    settings = {"font": "standard"}
    
    with caplog.at_level(logging.ERROR):
        result = run(settings)
    assert result is None
    assert "No text provided for the Figlet plugin" in caplog.text


#If invalid font, result is none

def test_invalid_font(caplog):

    settings = {"ascii_text": "hola", "font": "invalid_font"}

    with caplog.at_level(logging.ERROR):
        result = run(settings)
    assert result is None
    assert "Invalid font for the Figlet plugin" in caplog.text
