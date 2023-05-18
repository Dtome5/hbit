import typer
from rich import console
from Model import Habit
from database import store_habit, make_db, make_table

db = make_db("newdb.db")
make_table(db)

app = typer.Typer()
console = console.Console()


def add_habit(db, habit: Habit):
    cur = db.cursor()
    cur.execute("INSERT INTO Habits VALUES(:habit,:task) ",
                (habit.name, habit.task))


def show_habit(db, habit: Habit):
    cur = db.cursor()
    _ = cur.execute("SELECT habit, task FROM Habits")
    console.print(_.fetchall())
    return _.fetchall()


@app.command()
def main():
    hbit1 = Habit("read", "for four hours a day", (days := 2))
    add_habit(hbit1)
    typer.echo(show_habit(hbit1))
    print("yeah")


if __name__ == "__cli__":
    app.run(main)
