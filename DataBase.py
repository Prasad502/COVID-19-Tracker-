import sqlite3

def SignupData(Username,Password,Number,Email):
    try:
        connect = sqlite3.connect("storage.db")
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY, Username TEXT, Pass TEXT, PNumber Number, Email TEXT)")
        if (Username != "" and Password != "" and Number != "" and Email != ""):
            cursor.execute("INSERT INTO users(UserName, Pass, PNumber, Email) VALUES(?,?,?,?)",(Username,Password,Number,Email))
            connect.commit()
            connect.close()
            msg = "success"
            return msg
        else:
            msg = "failure"
            return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg

def LoginData(Username,Password):
    try:
        connect = sqlite3.connect("storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT Username,Pass FROM users WHERE Username =?", (Username,))
        get_password = cursor.fetchone()
        if Password == get_password[1] and Username == get_password[0]:
            connect.commit()
            msg = "success"
            connect.close()
            return msg
        else:
            msg = "failure"
            connect.close()
            return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg


def UpdatePass(Username,Pass):
    try:
        connect = sqlite3.connect("storage.db")
        cursor = connect.cursor()
        if (Pass != ""):
            cursor.execute("UPDATE users SET Pass = ? WHERE Username = ?",(Pass,Username))            
            connect.commit()
            connect.close()
            msg = "success"
            return msg
        else:
            msg = "failure"
            return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg
