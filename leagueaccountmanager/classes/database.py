from sqlite3 import connect as db_connect

class Database():
    def __init__(self):
        self.db = db_connect("./data.db")
        self.cursor = self.db.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS accounts (server VARCHAR(100), summoner VARCHAR(100), be INT, rp INT, soloQ VARCHAR(100), flexQ VARCHAR(100), username VARCHAR(100), password VARCHAR(100), accountId INT, summonerId INT, puuid VARCHAR(100), profileIconId INT);")

    def add_account(self, login, password):
        self.cursor.execute("INSERT INTO accounts (server, summoner, be, rp, soloq, flexq, username, password, accountId, summonerId, puuid, profileIconId) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", ("???", "?????", 0, 0, "?????", "?????", login, password, 0, 0, "?????", 0))
        self.db.commit()
    
    def list_accounts(self, server, elo):
        rows = []
        self.rows_count = 0
        for row in self.cursor.execute("SELECT * FROM accounts"):
            if row[0] == server or server == "ALL":
                if elo in row[4] or elo == "All":
                    rows.append(row)
                    self.rows_count += 1
        return rows

    def search_account(self, username):
        rows = []
        for row in self.cursor.execute("SELECT * FROM accounts WHERE username=?", (username,)):
            rows.append(row)
        return rows

    def first_login_update(self, server, summoner, be, rp, soloq, flexq, accountId, summonerId, puuid, profileIconId, username):
        self.cursor.execute("""
        UPDATE accounts SET
        server=?,
        summoner=?,
        be=?,
        rp=?,
        soloq=?,
        flexq=?,
        accountId=?,
        summonerId=?,
        puuid=?,
        profileIconId=?
        WHERE username=?
        """, (server, summoner, be, rp, soloq, flexq, accountId, summonerId, puuid, profileIconId, username))
        self.db.commit()

    def save_changes(self, server, summoner, be, rp, soloq, flexq, username, password, accountId, summonerId, puuid, profileIconId, temp_username):
        self.cursor.execute("""
        UPDATE accounts SET
        server=?,
        summoner=?,
        be=?,
        rp=?,
        soloq=?,
        flexq=?,
        username=?,
        password=?,
        accountId=?,
        summonerId=?,
        puuid=?,
        profileIconId=?
        WHERE username=?
        """, (server, summoner, be, rp, soloq, flexq, username, password, accountId, summonerId, puuid, profileIconId, temp_username))
        self.db.commit()

    def delete_account(self, username):
        self.cursor.execute("DELETE FROM accounts WHERE username=?", (username,))
        self.db.commit()