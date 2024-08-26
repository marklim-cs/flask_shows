import sqlite3

# connect to the db
conn = sqlite3.connect("shows.db")
cursor = conn.cursor()

# create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS shows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
)
''')

data = [
    ("Breaking Bad", "Vince Gilligan", 2008),
    ("Game of Thrones", "David Benioff and D.B. Weiss", 2011),
    ("Stranger Things", "The Duffer Brothers", 2016),
    ("The Crown", "Peter Morgan", 2016),
    ("The Office", "Greg Daniels", 2005),
    ("Friends", "David Crane and Marta Kauffman", 1994),
    ("The Mandalorian", "Jon Favreau", 2019),
    ("Sherlock", "Mark Gatiss and Steven Moffat", 2010),
    ("Westworld", "Jonathan Nolan and Lisa Joy", 2016),
    ("Narcos", "Chris Brancato, Carlo Bernard, and Doug Miro", 2015),
    ("Black Mirror", "Charlie Brooker", 2011),
    ("The Witcher", "Lauren Schmidt Hissrich", 2019),
    ("Money Heist", "Álex Pina", 2017),
    ("Fargo", "Noah Hawley", 2014),
    ("Better Call Saul", "Vince Gilligan and Peter Gould", 2015),
    ("The Big Bang Theory", "Chuck Lorre and Bill Prady", 2007),
    ("Dexter", "James Manos Jr.", 2006),
    ("True Detective", "Nic Pizzolatto", 2014),
    ("Ozark", "Bill Dubuque and Mark Williams", 2017),
    ("Vikings", "Michael Hirst", 2013),
    ("The Boys", "Eric Kripke", 2019),
    ("The Handmaid's Tale", "Bruce Miller", 2017),
    ("Chernobyl", "Craig Mazin", 2019),
    ("Rick and Morty", "Dan Harmon and Justin Roiland", 2013),
    ("Brooklyn Nine-Nine", "Michael Schur and Dan Goor", 2013),
    ("How I Met Your Mother", "Carter Bays and Craig Thomas", 2005),
    ("Supernatural", "Eric Kripke", 2005),
    ("The Simpsons", "Matt Groening", 1989),
    ("BoJack Horseman", "Raphael Bob-Waksberg", 2014),
    ("The X-Files", "Chris Carter", 1993),
    ("This Is Us", "Dan Fogelman", 2016),
    ("Grey's Anatomy", "Shonda Rhimes", 2005),
    ("The Marvelous Mrs. Maisel", "Amy Sherman-Palladino", 2017),
    ("Hannibal", "Bryan Fuller", 2013),
    ("GLOW", "Liz Flahive and Carly Mensch", 2017),
    ("The Expanse", "Mark Fergus and Hawk Ostby", 2015),
    ("Parks and Recreation", "Greg Daniels and Michael Schur", 2009),
    ("The Americans", "Joe Weisberg", 2013),
    ("Mad Men", "Matthew Weiner", 2007),
    ("Better Things", "Pamela Adlon and Louis C.K.", 2016),
    ("Narcos: Mexico", "Carlo Bernard, Chris Brancato, and Doug Miro", 2018),
    ("Castle Rock", "Sam Shaw and Dustin Thomason", 2018),
    ("Killing Eve", "Phoebe Waller-Bridge", 2018),
    ("The Umbrella Academy", "Steve Blackman", 2019),
    ("Penny Dreadful", "John Logan", 2014),
    ("Dark", "Baran bo Odar and Jantje Friese", 2017),
    ("GLOW", "Liz Flahive and Carly Mensch", 2017),
    ("The Good Place", "Michael Schur", 2016),
    ("Succession", "Jesse Armstrong", 2018),
    ("The Last Kingdom", "Stephen Butchard", 2015),
    ("Loki", "Michael Waldron", 2021),
    ("The Blacklist", "Jon Bokenkamp", 2013)
]

cursor.executemany("INSERT INTO shows (title, author, year) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()