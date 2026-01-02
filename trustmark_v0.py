import hashlib
import json
import os
from datetime import datetime, timezone



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "db.json")



def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(records):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def register(name: str, content: str):
   

    h = sha256(content)
    ts = datetime.now(timezone.utc).isoformat()
    record = {
        "name": name,
        "hash": h,
        "timestamp": ts
    }
    records = load_db()
    records.append(record)
    save_db(records)
    return record



def verify(content: str):
    h = sha256(content)
    records = load_db()
    matches = [r for r in records if r["hash"] == h]
    return h, matches


def main():
   
    print("TrustMark v0")
    mode = input("r=登録 / v=照合 : ").strip().lower()

    if mode == "r":
     name = input("名前: ")
     content = input("文章: ")
     record = register(name, content)

     print("✔ 登録しました")
     print(f"・登録者：{record['name']}")
     print(f"・登録日時：{record['timestamp']}")

    elif mode == "v":
     content = input("文章: ")
     h, matches = verify(content)

     if matches:
            r = matches[0]
            print("✔ 一致しました")
            print(f"・登録者：{r['name']}")
            print(f"・登録日時：{r['timestamp']}")
            print("・内容は変更されていません")
     else:
             print("✖ 見つかりません")
             print("・登録された内容と一致しません")

    else:
     print("r か v だけにしろ。選択肢は増やすな。")

if __name__ == "__main__":
    main()
