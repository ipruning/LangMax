import tiktoken


def test_tiktoken_encoding():
    # Test o200k_base encoding
    enc_base = tiktoken.get_encoding("o200k_base")
    assert enc_base.decode(enc_base.encode("hello world")) == "hello world"

    # Test gpt-4o model encoding
    enc_gpt4 = tiktoken.encoding_for_model("gpt-4o")

    # Test encoding and decoding
    encoded = enc_gpt4.encode("hello world")
    decoded = enc_gpt4.decode(encoded)

    assert isinstance(encoded, list), "Encoded result should be a list"
    assert all(isinstance(token, int) for token in encoded), "All tokens should be integers"
    assert decoded == "hello world", "Decoded result should match original input"
