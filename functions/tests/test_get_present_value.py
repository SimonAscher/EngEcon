import pytest

from functions import present_value

def test_get_pv_av_case():
    assert present_value(value=1234, value_type="AV", interest_rate=0.05,
                         discount_period=20) == pytest.approx(15378.367562694)

def test_get_pv_fv_case():
    assert present_value(value=5678, value_type="FV", interest_rate=0.05,
                         discount_period=20) == pytest.approx(2139.9784837529)

def test_get_pv_other_str_case():
    with pytest.raises(ValueError):
        present_value(value=3000, value_type="Wrong String")
