import sys, pathlib, datetime
DB = pathlib.Path("notes.txt")

def add(note):
    with DB.open("a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now().isoformat(timespec='seconds')}] {note}\n")

def list_notes():
    print(DB.read_text(encoding="utf-8") if DB.exists() else "No notes yet.")

def search(q):
    if not DB.exists(): return print("No notes yet.")
    for line in DB.read_text(encoding="utf-8").splitlines():
        if q.lower() in line.lower(): print(line)

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: add|list|search"); raise SystemExit
    cmd,*args = sys.argv[1:]
    if cmd=="add": add(" ".join(args))
    elif cmd=="list": list_notes()
    elif cmd=="search": search(" ".join(args))
