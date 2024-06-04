import tiktoken

if __name__ == "__main__":
    enc = tiktoken.get_encoding("o200k_base")
    print(enc.decode([193825]))
    print(enc.decode([185118]))
