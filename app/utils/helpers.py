def clear_screen():
    print("\n" + "=" * 60 + "\n")


def multiline_read(prompt: str = ""):
    if prompt:
        print(prompt)
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)


def get_next_id(prefix: str, table: str):
    from app.core.database import execute
    row = execute(f"SELECT id FROM {table} ORDER BY id DESC LIMIT 1", fetch = "one")

    if not row:
        return f"{prefix}001"
    num = int(row["id"][len(prefix):])
    return f"{prefix}{num + 1:03d}"