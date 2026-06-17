import sqlite3

conn = sqlite3.connect("characters.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS characters(
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    char_class TEXT,
    race TEXT,
    history TEXT,
    skills TEXT,
    items TEXT
)
""")

conn.commit()


def save_character(user_id, data):
    cursor.execute("""
    INSERT OR REPLACE INTO characters
    (user_id, name, char_class, race, history, skills, items)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        data["name"],
        data["char_class"],
        data["race"],
        data["history"],
        data["skills"],
        data["items"]
    ))

    conn.commit()


def get_character(user_id):
    cursor.execute(
        "SELECT * FROM characters WHERE user_id=?",
        (user_id,)
    )
    return cursor.fetchone()