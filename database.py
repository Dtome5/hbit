import sqlite3
import datetime
from Model import Habit
from datetime import date, timedelta


def make_db(name="hbit.db"):
    data = sqlite3.connect(name,
                           detect_types=sqlite3.PARSE_DECLTYPES
                           | sqlite3.PARSE_COLNAMES)
    return data


def make_table(db):
    cur = db.cursor()
    _ = cur.execute("CREATE TABLE IF NOT EXISTS Habits(habit , task)")
    db.commit()
    return


def store_habit(db, habit: Habit):
    """Stores habit's name, task, periodicity into a database"""
    db = make_db()
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Habits(habit , task)")
    cur.execute(
        "INSERT INTO Habits VALUES(:habit, :task)",
        (habit.name, habit.task),
    )
    db.commit()


def get_habit(db, habit: Habit):
    """Selects and returns row containing habit's name."""
    cur = db.cursor()
    _ = cur.execute("SELECT task FROM Habits WHERE task = ?", (habit.task, ))
    return _.fetchall()


def check_habit(db, habit: Habit, status):
    """Stores the habit as done on the date of completion"""
    cur = db.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Status(habit text, checked bool, date date)"
    )
    cur.execute("INSERT INTO Status Values (:habit, :checked, :date)",
                (habit.name, status, datetime.date(2023, 5, 11)))
    db.commit()
    _ = cur.execute("SELECT checked FROM Status")
    return _.fetchall()


def update(db, habit: Habit):
    cur = db.cursor()
    _ = cur.execute("SELECT date from Status ORDER BY date")
    prevdb_date = _.fetchone()
    prev_date = prevdb_date[0]
    date_now = date.today()
    if prev_date >= date_now:
        pass
    else:
        inter_date = prev_date
        while inter_date <= date_now:
            cur.execute("""INSERT INTO Status VALUES(:habit,:date,:checked)""",
                        (habit.name, inter_date, False))
            inter_date += timedelta(days=1)
            db.commit()
    return prev_date


def get_Status(db):
    cur = db.cursor()
    _ = cur.execute("SELECT date FROM Status")
    return _.fetchall()


db = make_db(":memory:")
make_table(db)
habit1 = Habit("read", "read four hours a day", (days := 1))
check_habit(db, habit1, True)
print(get_Status(db))
cur = db.cursor()
res = cur.execute("select * from Status")
print(res.fetchall())
print(update(db, habit1))
