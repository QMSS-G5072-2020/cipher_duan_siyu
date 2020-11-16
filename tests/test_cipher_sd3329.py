from cipher_sd3329 import __version__
from cipher_sd3329 import cipher_sd3329

def test_version():
    assert __version__ == '0.1.0'

def test_cipher_with_word():
    example = 'Columbia'
    expected = 'Dpmvncjb'
    actual = cipher_sd3329.cipher(example, 1)
    assert expected == actual, 'Should be True'