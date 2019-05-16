#!/usr/bin/python

"""
Tests for geom.py
"""
import pytest
import geom

def test_cal_dis():
    coord1 = [0,0,2]
    coord2 = [0,0,0]

    obs = geom.cal_dis(coord1,coord2)

    assert obs == 2.0

def test_bcheck_f():
    """A test for the bond_check fxn"""
    b_len = 3.0
    obs = geom.bond_check(b_len)
    assert obs == False

def test_bcheck_t():
    b_len = 1.4
    obs = geom.bond_check(b_len)
    assert obs == True

def test_err():
    b_len = 'a'

    with pytest.raises(TypeError):
        obs = geom.bond_check(b_len)
