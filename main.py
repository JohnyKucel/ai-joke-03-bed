import os

JOKE = "Me and my bed are soulmates; the alarm clock is just the homewrecker."

def resolve_output_dir():
    out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip() or "/output"
    out_dir = os.path.abspath(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    return out_dir

def write_entry(out_dir, text):
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return path

def main():
    out_dir = resolve_output_dir()
    write_entry(out_dir, JOKE)

if __name__ == "__main__":
    main()
