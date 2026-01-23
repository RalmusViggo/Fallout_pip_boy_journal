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

@app.route('/factions/legion')
def legion():
    return render_template("factions/legion.html")

@app.route('/factions/ncr')
def ncr():
    return render_template("factions/ncr.html")

@app.route('/creatures')
def creatures():
    return render_template("creatures.html")

@app.route('/creatures/mutants')
def creatures_mutants():
    return render_template("creatures_dir/mutants.html")

@app.route('/creatures/deathclaw')
def creatures_deathclaw():
    return render_template("creatures_dir/deathclaw.html")

@app.route('/creatures/ghouls')
def creatures_ghouls():
    return render_template("creatures_dir/ghouls.html")

@app.route('/creatures/radscorpion')
def creatures_radscorpion():
    return render_template("creatures_dir/radscorpion.html")

@app.route('/creatures/yao_guai')
def creatures_yao_guai():
    return render_template("creatures_dir/yao_guai.html")

@app.route('/creatures/vermin')
def creatures_vermin():
    return render_template("creatures_dir/vermin.html")

@app.route('/creatures/aquatic')
def creatures_aquatic():
    return render_template("creatures_dir/aquatic.html")

@app.route('/creatures/hoofed_mammals')
def creatures_hoofed_mammals():
    return render_template("creatures_dir/hoofed_mammals.html")

@app.route('/creatures/arthropods')
def creatures_arthropods():
    return render_template("creatures_dir/arthropods.html")

@app.route('/creatures/canines')
def creatures_canines():
    return render_template("creatures_dir/canines.html")

@app.route('/creatures/gecko')
def creatures_gecko():
    return render_template("creatures_dir/gecko.html")

@app.route('/creatures/mutants/super')
def super():
    return render_template("creatures_dir/mutants/super.html")

@app.route('/creatures/mutants/nightkin')
def nightkin():
    return render_template("creatures_dir/mutants/nightkin.html")
@app.route('/creatures/mutants/centaurs')
def centaur():
    return render_template("creatures_dir/mutants/centaurs.html")


@app.route('/creatures/aquatic_creatures/mirelurks')
def mirelurks():
    return render_template("creatures_dir/aquatic_creatures/mirelurks.html")

@app.route('/creatures/aquatic_creatures/gulper')
def gulper():
    return render_template("creatures_dir/aquatic_creatures/gulper.html")

@app.route('/creatures/aquatic_creatures/angler')
def angler():
    return render_template("creatures_dir/aquatic_creatures/angler.html")

@app.route('/creatures/arthropods_creatures/bloatfly')
def bloatfly():
    return render_template("creatures_dir/arthropods_creatures/bloatfly.html")

@app.route('/creatures/arthropods_creatures/bloodbug')
def bloodbug():
    return render_template("creatures_dir/arthropods_creatures/bloodbug.html")

@app.route('/creatures/arthropods_creatures/cazador')
def cazador():
    return render_template("creatures_dir/arthropods_creatures/cazador.html")

@app.route('/creatures/arthropods_creatures/giant_ant')
def giant_ant():
    return render_template("creatures_dir/arthropods_creatures/giant_ant.html")

@app.route('/creatures/arthropods_creatures/radroach')
def radroach():
    return render_template("creatures_dir/arthropods_creatures/radroach.html")

@app.route('/creatures/arthropods_creatures/radscorpion')
def radscorpion():
    return render_template("creatures_dir/arthropods_creatures/radscorpion.html")

@app.route('/creatures/canines_creatures/dog')
def dog():
    return render_template("creatures_dir/canines_creatures/dog.html")

@app.route('/creatures/canines_creatures/mongrel')
def mongrel():
    return render_template("/creatures_dir/canines_creatures/mongrel.html")

@app.route('/creatures/canines_creatures/mutant_hound')
def mutant_hound():
    return render_template("/creatures_dir/canines_creatures/mutant_hound.html")

@app.route('/creatures/canines_creatures/wolf')
def wolf():
    return render_template("/creatures_dir/canines_creatures/wolf.html")

@app.route('/creatures/canines_creatures/cyberdog')
def cyberdog():
    return render_template("/creatures_dir/canines_creatures/cyberdog.html")

@app.route('/creatures/ghouls/glowing_one')
def glowing_one():
    return render_template("/creatures_dir/glowing_one.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

if __name__ == "__main__":
    app.run()
