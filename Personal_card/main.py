import json
import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/member')
def random_member():
    with open('../Personal_card/templates/crew.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        crew_member = random.choice(data)
        member_name = f"{crew_member['name']} {crew_member['surname']}"
        member_photo = "static/img/" + crew_member['photo']
        specialties = ", ".join(sorted(crew_member['speciality']))
        return render_template('member.html', name=member_name, photo=member_photo, specialties=specialties)


if __name__ == '__main__':
    app.run()
