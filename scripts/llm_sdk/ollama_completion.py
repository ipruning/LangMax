import re
from typing import List

import requests
from openai import OpenAI
from tiktoken import encoding_for_model

OLLAMA_API_KEY = "ollama"
OLLAMA_API_BASE_URL = "http://localhost:11434/v1/"
OLLAMA_MODEL = "reader-lm:1.5b"


encoding = encoding_for_model("gpt-4o-mini")

client = OpenAI(
    base_url=OLLAMA_API_BASE_URL,
    api_key=OLLAMA_API_KEY,
)


def get_html_content(url):
    api_url = f"https://r.jina.ai/{url}"
    headers = {"X-Return-Format": "html"}
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"error: {str(e)}"


def create_prompt(text: str, tokenizer) -> str:
    messages = [
        {"role": "user", "content": text},
    ]
    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)


# (REMOVE <SCRIPT> to </script> and variations)
SCRIPT_PATTERN = r"<[ ]*script.*?\/[ ]*script[ ]*>"  # mach any char zero or more times
# text = re.sub(pattern, '', text, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

# (REMOVE HTML <STYLE> to </style> and variations)
STYLE_PATTERN = r"<[ ]*style.*?\/[ ]*style[ ]*>"  # mach any char zero or more times
# text = re.sub(pattern, '', text, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

# (REMOVE HTML <META> to </meta> and variations)
META_PATTERN = r"<[ ]*meta.*?>"  # mach any char zero or more times
# text = re.sub(pattern, '', text, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

# (REMOVE HTML COMMENTS <!-- to --> and variations)
COMMENT_PATTERN = r"<[ ]*!--.*?--[ ]*>"  # mach any char zero or more times
# text = re.sub(pattern, '', text, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

# (REMOVE HTML LINK <LINK> to </link> and variations)
LINK_PATTERN = r"<[ ]*link.*?>"  # mach any char zero or more times

# (REPLACE base64 images)
BASE64_IMG_PATTERN = r'<img[^>]+src="data:image/[^;]+;base64,[^"]+"[^>]*>'

# (REPLACE <svg> to </svg> and variations)
SVG_PATTERN = r"(<svg[^>]*>)(.*?)(<\/svg>)"


def replace_svg(html: str, new_content: str = "this is a placeholder") -> str:
    return re.sub(
        SVG_PATTERN,
        lambda match: f"{match.group(1)}{new_content}{match.group(3)}",
        html,
        flags=re.DOTALL,
    )


def replace_base64_images(html: str, new_image_src: str = "#") -> str:
    return re.sub(BASE64_IMG_PATTERN, f'<img src="{new_image_src}"/>', html)


def has_base64_images(text: str) -> bool:
    base64_content_pattern = r'data:image/[^;]+;base64,[^"]+'
    return bool(re.search(base64_content_pattern, text, flags=re.DOTALL))


def has_svg_components(text: str) -> bool:
    return bool(re.search(SVG_PATTERN, text, flags=re.DOTALL))


def clean_html(html: str, clean_svg: bool = False, clean_base64: bool = False):
    html = re.sub(SCRIPT_PATTERN, "", html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
    html = re.sub(STYLE_PATTERN, "", html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
    html = re.sub(META_PATTERN, "", html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
    html = re.sub(COMMENT_PATTERN, "", html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
    html = re.sub(LINK_PATTERN, "", html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    if clean_svg:
        html = replace_svg(html)

    if clean_base64:
        html = replace_base64_images(html)

    return html


def naive_chunking(prompt: str, max_chars: int) -> List[str]:
    return [prompt[i : i + max_chars] for i in range(0, len(prompt), max_chars)]


def naive_inference(prompt: str) -> str:
    chunks = naive_chunking(prompt, 2048)
    print(chunks)
    cleaned: list[str] = []

    for chunk in chunks:
        completion = client.chat.completions.create(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": chunk,
                },
            ],
            max_tokens=512,
        )

        res = completion.choices[0].message.content
        if res is None:
            res = ""

        cleaned.append(res)

        print(res)

    return "".join(cleaned)


url = ""
print(f"We will use Jina Reader to fetch the **raw HTML** from: {url}")
html = get_html_content(url)
html = clean_html(html, clean_svg=True, clean_base64=True)
naive_inference(html)
