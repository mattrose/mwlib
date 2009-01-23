#! /usr/bin/env py.test

from mwlib.expander import parse

def test_no_arguments():
    t = parse(u"{{bla}}")
    assert t[1]==(), "expected an empty tuple"

    
def test_one_empty_arguments():
    t = parse(u"{{bla|}}")
    assert t[1]==(u""), "expected exactly one empty argument"
    
    
