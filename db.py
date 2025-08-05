
import sqlite3

DB_FILE = "aov.db"

def connect():
    return sqlite3.connect(DB_FILE)

def get_player(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM players WHERE name=?", (name,))
    player_row = cur.fetchone()
    if not player_row:
        conn.close()
        return None

    player = {
        "level": player_row[1],
        "win_rate": player_row[2],
        "matches": [],
        "skins": []
    }

    cur.execute("SELECT result, hero, kills, deaths FROM matches WHERE player_name=?", (name,))
    matches = cur.fetchall()
    for match in matches:
        player["matches"].append({
            "result": match[0],
            "hero": match[1],
            "kills": match[2],
            "deaths": match[3]
        })

    cur.execute("SELECT skin_name FROM skins WHERE player_name=?", (name,))
    skins = cur.fetchall()
    player["skins"] = [s[0] for s in skins]

    conn.close()
    return player

def add_player(name, level, win_rate):
    conn = connect()
    try:
        conn.execute("INSERT INTO players (name, level, win_rate) VALUES (?, ?, ?)", (name, level, win_rate))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def add_match(name, result, hero, kills, deaths):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM players WHERE name=?", (name,))
    if not cur.fetchone():
        conn.close()
        return False
    cur.execute("INSERT INTO matches (player_name, result, hero, kills, deaths) VALUES (?, ?, ?, ?, ?)",
                (name, result, hero, kills, deaths))
    conn.commit()
    conn.close()
    return True

def add_skin(name, skin_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM players WHERE name=?", (name,))
    if not cur.fetchone():
        conn.close()
        return False
    cur.execute("INSERT INTO skins (player_name, skin_name) VALUES (?, ?)", (name, skin_name))
    conn.commit()
    conn.close()
    return True
