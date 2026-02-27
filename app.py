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

@app.route('/register_actual', methods=['GET', 'POST'])
def register_actual():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        origin = form.origin.data
        origin_trait = form.origin_trait.data
        strength = form.strength.data
        perception = form.perception.data
        endurance = form.endurance.data
        charisma = form.charisma.data
        intelligence = form.intelligence.data
        agility = form.agility.data
        luck = form.luck.data
        tagskill1 = form.tagskill1.data
        tagskill2 = form.tagskill2.data
        tagskill3 = form.tagskill3.data
        athletics = form.athletics.data
        barter = form.barter.data
        big_guns = form.big_guns.data
        energy_weapons = form.energy_weapons.data
        explosives = form.explosives.data
        lockpick = form.lockpick.data
        medicine = form.medicine.data
        melee_weapons = form.melee_weapons.data
        pilot = form.pilot.data
        repair = form.repair.data
        science = form.science.data
        small_guns = form.small_guns.data
        sneak = form.sneak.data
        speech = form.speech.data
        survival = form.survival.data
        throwing = form.throwing.data
        unarmed = form.unarmed.data
        level = form.level.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password, origin, origin_trait, strength, perception, endurance, charisma, intelligence, agility, luck, tagskill1, tagskill2, tagskill3, athletics, barter, big_guns, energy_weapons, explosives, lockpick, medicine, melee_weapons, pilot, repair, science, small_guns, sneak, speech, survival, throwing, unarmed, level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (username,password,origin,origin_trait,strength,perception,endurance,charisma,intelligence,agility,luck,tagskill1,tagskill2,tagskill3,athletics,barter,big_guns,energy_weapons,explosives,lockpick,medicine,melee_weapons,pilot,repair,science,small_guns,sneak,speech,survival,throwing,unarmed,level)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect("/")
    return render_template("register_actual.html", form=form)



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

@app.route('/factions/institute')
def institute():
    return render_template("factions/institute.html")

@app.route('/factions/minutemen')
def minutemen():
    return render_template("factions/minutemen.html")

@app.route('/factions/railroad')
def railroad():
    return render_template("factions/railroad.html")

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

@app.route('/creatures/glowing_one')
def creatures_glowing_one():
    return render_template("/creatures_dir/glowing_one.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

@app.route('/creatures/hoofed_mammals_creatures/bighorner')
def bighorner():
    return render_template("/creatures_dir/hoofed_mammals_creatures/bighorner.html")

@app.route('/creatures/hoofed_mammals_creatures/brahmin')
def brahmin():
    return render_template("/creatures_dir/hoofed_mammals_creatures/brahmin.html")

@app.route('/creatures/hoofed_mammals_creatures/radstag')
def radstag(): 
    return render_template("/creatures_dir/hoofed_mammals_creatures/radstag.html")

@app.route('/creatures/vermin/giant_rat')
def giant_rat():
    return render_template("/creatures_dir/vermin_creatures/giant_rat.html")

@app.route('/creatures/vermin/mole_rat')
def mole_rat():
    return render_template("/creatures_dir/vermin_creatures/mole_rat.html")

@app.route('/creatures/vermin/nightstalker')
def nightstalker(): 
    return render_template("/creatures_dir/vermin_creatures/nightstalker.html")

@app.route('/creatures/non-feral')
def nonferal():
    return render_template("/creatures_dir/non-feral.html")

@app.route('/stats')
def stats():
    return render_template("stats.html")

@app.route('/journal_entries')
def journal_entries():
    return render_template("journal_entries.html")

@app.route('/journal/journal_west_coast')
def journal_west_coast():
    return render_template("journal/journal_west_coast.html")

@app.route('/journal/journal_commonwealth')
def journal_commonwealth():
    return render_template("journal/journal_commonwealth.html")

@app.route('/journal/journal_capital')
def journal_capital():
    return render_template("journal/journal_capital.html")

@app.route('/journal/journal_appalachia')
def journal_appalachia():
    return render_template("journal/journal_appalachia.html")

if __name__ == "__main__":
    app.run()
