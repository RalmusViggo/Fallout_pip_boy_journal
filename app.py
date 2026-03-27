from flask import Flask, render_template_string, render_template, request, redirect, url_for, session
import mysql.connector
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import requests



app = Flask(__name__)
app.secret_key = "123"

def get_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="rasmus",
        password="R-asmus150508",
        database="vault186"
    )
    return conn


@app.route('/')
def index():
    api_response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = api_response.json()["value"]
    date = api_response.json()["updated_at"]
    img = "https://cataas.com/cat"
    return render_template("index.html", joke=joke, date=date, img=img)

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

        password_hash = generate_password_hash(password)
        
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password, origin, origin_trait, strength, perception, endurance, charisma, intelligence, agility, luck, tagskill1, tagskill2, tagskill3, athletics, barter, big_guns, energy_weapons, explosives, lockpick, medicine, melee_weapons, pilot, repair, science, small_guns, sneak, speech, survival, throwing, unarmed, level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (username,password_hash,origin,origin_trait,strength,perception,endurance,charisma,intelligence,agility,luck,tagskill1,tagskill2,tagskill3,athletics,barter,big_guns,energy_weapons,explosives,lockpick,medicine,melee_weapons,pilot,repair,science,small_guns,sneak,speech,survival,throwing,unarmed,level)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect("/")
    return render_template("register_actual.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT username, password FROM users WHERE username=%s",
            (username,)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            password_db = user[1]
        if check_password_hash(password_db, password):
            session['username'] = user[0]  # lagrer navnet i session
            return redirect("/")
        else:
            form.username.errors.append("Invalid username or password")

    return render_template("login.html", form=form)

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

@app.route('/factions/enclave')
def enclave():
    return render_template("factions/enclave.html")

@app.route('/factions/legion')
def legion():
    return render_template("factions/legion.html")

@app.route('/factions/ncr')
def ncr():
    return render_template("factions/ncr.html")

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

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    # always use lowercase variable names and the Flask session helpers
    username = session.get('username')  # hent navn fra session
    origin = session.get('origin')
    origin_trait = session.get('origin_trait')
    strength = session.get('strength')
    perception = session.get('perception')
    endurance = session.get('endurance')
    charisma = session.get('charisma')
    intelligence = session.get('intelligence')
    agility = session.get('agility')
    luck = session.get('luck')
    tagskill1 = session.get('tagskill1')
    tagskill2 = session.get('tagskill2')
    tagskill3 = session.get('tagskill3')
    athletics = session.get('athletics')
    barter = session.get('barter')
    big_guns = session.get('big_guns')
    energy_weapons = session.get('energy_weapons')
    explosives = session.get('explosives')
    lockpick = session.get('lockpick')
    medicine = session.get('medicine')
    melee_weapons = session.get('melee_weapons')
    pilot = session.get('pilot')
    repair = session.get('repair')
    science = session.get('science')
    small_guns = session.get('small_guns')
    sneak = session.get('sneak')
    speech = session.get('speech')
    survival = session.get('survival')
    throwing = session.get('throwing')
    unarmed = session.get('unarmed')
    level = session.get('level')
    
    if not username:
        return redirect(url_for('login'))
    # render page, `name` passed directly into template
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
            """ SELECT username,
            origin,
            origin_trait,
            strength,
            perception,
            endurance,
            charisma,
            intelligence,
            agility,
            luck,
            tagskill1,
            tagskill2,
            tagskill3,
            athletics,
            barter,
            big_guns,
            energy_weapons,
            explosives,
            lockpick,
            medicine,
            melee_weapons,
            pilot,
            repair,
            science,
            small_guns,
            sneak,
            speech,
            survival,
            throwing,
            unarmed,
            level 
            FROM
            users
            WHERE
            username=%s""",
            (username,)
        )
    stat = cur.fetchall()
    cur.close()
    conn.close()
    session['origin'] = stat[0][1] if stat else None
    session['origin_trait'] = stat[0][2] if stat else None
    session['strength'] = stat[0][3] if stat else None
    session['perception'] = stat[0][4] if stat else None
    session['endurance'] = stat[0][5] if stat else None
    session['charisma'] = stat[0][6] if stat else None
    session['intelligence'] = stat[0][7] if stat else None
    session['agility'] = stat[0][8] if stat else None
    session['luck'] = stat[0][9] if stat else None
    session['tagskill1'] = stat[0][10] if stat else None
    session['tagskill2'] = stat[0][11] if stat else None
    session['tagskill3'] = stat[0][12] if stat else None
    session['athletics'] = stat[0][13] if stat else None
    session['barter'] = stat[0][14] if stat else None
    session['big_guns'] = stat[0][15] if stat else None
    session['energy_weapons'] = stat[0][16] if stat else None
    session['explosives'] = stat[0][17] if stat else None
    session['lockpick'] = stat[0][18] if stat else None
    session['medicine'] = stat[0][19] if stat else None
    session['melee_weapons'] = stat[0][20] if stat else None
    session['pilot'] = stat[0][21] if stat else None
    session['repair'] = stat[0][22] if stat else None
    session['science'] = stat[0][23] if stat else None
    session['small_guns'] = stat[0][24] if stat else None
    session['sneak'] = stat[0][25] if stat else None
    session['speech'] = stat[0][26] if stat else None
    session['survival'] = stat[0][27] if stat else None
    session['throwing'] = stat[0][28] if stat else None
    session['unarmed'] = stat[0][29] if stat else None
    session['level'] = stat[0][30] if stat else None
    health = endurance + luck + (level -1 )
    
    # Create a dictionary of skills for easy modification
    skill_dict = {
        'athletics': athletics,
        'barter': barter,
        'big_guns': big_guns,
        'energy_weapons': energy_weapons,
        'explosives': explosives,
        'lockpick': lockpick,
        'medicine': medicine,
        'melee_weapons': melee_weapons,
        'pilot': pilot,
        'repair': repair,
        'science': science,
        'small_guns': small_guns,
        'sneak': sneak,
        'speech': speech,
        'survival': survival,
        'throwing': throwing,
        'unarmed': unarmed
    }
    
    # Add +2 to each tag skill
    for tag in [tagskill1, tagskill2, tagskill3]:
        if tag and tag in skill_dict:
            skill_dict[tag] += 2
    
    # Update the variables from the dictionary
    athletics = skill_dict['athletics']
    barter = skill_dict['barter']
    big_guns = skill_dict['big_guns']
    energy_weapons = skill_dict['energy_weapons']
    explosives = skill_dict['explosives']
    lockpick = skill_dict['lockpick']
    medicine = skill_dict['medicine']
    melee_weapons = skill_dict['melee_weapons']
    pilot = skill_dict['pilot']
    repair = skill_dict['repair']
    science = skill_dict['science']
    small_guns = skill_dict['small_guns']
    sneak = skill_dict['sneak']
    speech = skill_dict['speech']
    survival = skill_dict['survival']
    throwing = skill_dict['throwing']
    unarmed = skill_dict['unarmed']
    
    return render_template("stats.html", name=username, health=health, stat=stat, origin=origin, origin_trait=origin_trait, strength=strength, perception=perception, endurance=endurance, charisma=charisma, intelligence=intelligence, agility=agility, luck=luck, tagskill1=tagskill1, tagskill2=tagskill2, tagskill3=tagskill3, athletics=athletics, barter=barter, big_guns=big_guns, energy_weapons=energy_weapons, explosives=explosives, lockpick=lockpick, medicine=medicine, melee_weapons=melee_weapons, pilot=pilot, repair=repair, science=science, small_guns=small_guns, sneak=sneak, speech=speech, survival=survival, throwing=throwing, unarmed=unarmed, level=level)

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

@app.route('/journal/journal_mojave_nevada')
def journal_mojave_nevada():
    return render_template("journal/journal_mojave_nevada.html")

@app.route('/char')
def char():
    return render_template("char.html")

@app.route('/glow')
def glow():
    return render_template("glow.html")



if __name__ == "__main__":
    app.run(port=8080, debug=True)
