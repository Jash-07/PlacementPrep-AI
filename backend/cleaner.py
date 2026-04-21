import re

def clean_text(paragraphs: list[str]) -> str:
    cleaned = []

    for p in paragraphs:
        # Remove citations like [1], [23]
        p = re.sub(r"\[\d+\]", "", p)

        # Remove extra spaces
        p = re.sub(r"\s+", " ", p)

        # Remove weird characters
        p = p.replace("\xa0", " ").strip()

        if len(p) > 50:  # filter very small/noisy lines
            cleaned.append(p)

    # Join into one large text block
    return "\n".join(cleaned[:20])  # limit size for now