from flask import Flask, render_template_string, render_template, request, redirect, url_for
import mysql.connector
from forms import RegisterForm

app = Flask(__name__)
app.secret_key = "123"

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="rasmus",
        password="R-asmus150508",
        database="vault186"
    )

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        gender = form.gender.data
        age = form.age.data
        blood_type = form.blood_type.data
        known_diseases = form.known_diseases.data
        family = form.family.data
        current_medical_conditions = form.current_medical_conditions.data
        previous_medical_conditions = form.previous_medical_conditions.data
        allergies = form.allergies.data
        strengths = form.strengths.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO inhabitant_data (name, gender, age, blood_type, known_diseases, family, current_medical_conditions, previous_medical_conditions, allergies, strengths) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, gender, age, blood_type, known_diseases, family, current_medical_conditions, previous_medical_conditions, allergies, strengths)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect("/")
    return render_template("register.html", form=form)

@app.route('/factions')
def factions():
    return render_template("factions.html")

@app.route('/factions/atomites')
def atomites():
    return render_template("factions/atomites.html")

@app.route('/factions/mutants')
def mutants():
    return render_template("factions/mutants.html")

@app.route('/factions/bos')
def bos():
    return render_template("factions/bos.html")

@app.route('/factions/caravans')
def caravans():
    return render_template("factions/caravans.html")

@app.route('/factions/raiders')
def raiders():
    return render_template("factions/raiders.html") 

@app.route('/factions/vault_dwellers')
def vault_dwellers():
    return render_template("factions/vault_dwellers.html")

@app.route('/factions/enclave')
def enclave():
    return render_template("factions/enclave.html")


if __name__ == "__main__":
    app.run()