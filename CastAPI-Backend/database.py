import sqlite3

class database:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.con = self.connection.cursor()

        self.con.execute('''create table if not exists user
                         (id integer primary key autoincrement, username text not null, name text)''')
        
        self.con.execute('''create table if not exists chat
                          (id integer primary key autoincrement, chatName text, createdOn text)''')
        
        self.con.execute('''create table if not exists message
                          chatID integer, userID integer, messageContent text, media text, datePublished text,
                          foreign key (chatID) references chat(id),
                          foreign key (userID) references user(id)''')