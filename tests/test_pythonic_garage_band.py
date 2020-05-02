import pytest
from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Musician, Guitarist, Bassist, Drummer, Band

def test_version():
    assert __version__ == '0.1.0'

def test_band_created_instances(some_band):
    assert Band.to_list() == [some_band]

def test_band_name_attribute():
    with pytest.raises(TypeError):
        some_band = Band()
    
    with pytest.raises(TypeError):
        some_band = Band("name")
    
    with pytest.raises(TypeError):
        some_band = Band([], [])

def test_band_members_attribute():
    with pytest.raises(TypeError):
        some_band = Band("name")
    
    with pytest.raises(TypeError):
        some_band = Band("name", "invalid")
    
    with pytest.raises(TypeError):
        some_band = Band("name", [1, 2, 3])
    
    with pytest.raises(TypeError):
        some_band = Band("name", [])

def test_guitarist():
    hux = Guitarist("Chen Hu")
    assert hux.name == "Chen Hu"
    assert hux.get_instrument() == "guitar"
    assert hux.play_solo() == "playing Europe"
    assert str(hux) == "I'm a guitarist"
    assert repr(hux) == "Guitarist instance"

def test_bassist():
    simon = Bassist("Simon")
    assert simon.name == "Simon"
    assert simon.get_instrument() == "bass"
    assert simon.play_solo() == "playing My Generation"
    assert str(simon) == "I'm a bassist"
    assert repr(simon) == "Bassist instance"

def test_drummer():
    hua = Drummer("Hua Zi")
    assert hua.name == "Hua Zi"
    assert hua.get_instrument() == "drum"
    assert hua.play_solo() == "playing Rush"
    assert str(hua) == "I'm a drummer"
    assert repr(hua) == "Drummer instance"

def test_custom_solo_guitar():
    solo = "some guitar solo"
    guitarist = Guitarist("name", solo)
    assert guitarist.solo == solo

def test_custom_solo_bass():
    solo = "some bass solo"
    bassist = Bassist("name", solo)
    assert bassist.solo == solo

def test_custom_solo_drum():
    solo = "some drum solo"
    drummer = Drummer("name", solo)
    assert drummer.solo == solo

def test_play_solos(some_band):
    assert some_band.name == "Yellow Giant"
    assert some_band.play_solos() == ["playing Europe", "playing My Generation", "playing Rush"]

@pytest.fixture
def some_band():
    yellowGiant = Band(
        "Yellow Giant",
        [Guitarist("Chen Hu"), Bassist("Simon"), Drummer("Hua Zi")]
    )
    return yellowGiant

def test_band_to_str(some_band):
    assert str(some_band.__str__()) == "The Yellow Giant band with members: Chen Hu, Simon, Hua Zi"

def test_band_repr(some_band):
    assert repr(some_band) == "Band instance"


