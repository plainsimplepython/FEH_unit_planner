import sqlite3


# TODO remove drop table clauses
def create_database(data):
    connection = sqlite3.connect('./FEH_characters.db')
    cursor = connection.cursor()

    # cursor.execute('DROP TABLE IF EXISTS Character')
    try:
        cursor.execute('''CREATE TABLE Character (id INTEGER PRIMARY KEY,
                                                  name TEXT,
                                                  title TEXT,
                                                  image_id INT UNIQUE,
                                                  description TEXT,
                                                  rarity TEXT,
                                                  acquisition TEXT,
                                                  blessing_type TEXT,
                                                  blessing_boost TEXT,
                                                  duo_skill TEXT,
                                                  duel TEXT,
                                                  pair_up TEXT,
                                                  weapon_type TEXT,
                                                  move_type TEXT,
                                                  hp TEXT,
                                                  atk TEXT,
                                                  spd TEXT,
                                                  def TEXT,
                                                  res TEXT,
                                                  total TEXT,
                                                  weapons TEXT,
                                                  assists TEXT,
                                                  specials TEXT,
                                                  passives TEXT,
                                                  FOREIGN KEY (image_id) REFERENCES Character_Images (image_id))''')
    except sqlite3.OperationalError:
        pass


    # cursor.execute('DROP TABLE IF EXISTS Character_Images')
    try:    # TODO compress image table into CSV string?
        cursor.execute('''CREATE TABLE Character_Images (image_id INTEGER PRIMARY KEY,
                                                      portrait TEXT,
                                                      attack TEXT, 
                                                      special TEXT,
                                                      injured TEXT)''')
    except sqlite3.OperationalError:
        pass


    # cursor.execute('DROP TABLE IF EXISTS Character_Stats')
    # cursor.execute('''CREATE TABLE Character_Stats (stats_id INTEGER PRIMARY KEY,
    #                                                 hp TEXT,
    #                                                 atk TEXT,
    #                                                 spd TEXT,
    #                                                 def TEXT,
    #                                                 res TEXT,
    #                                                 total TEXT)''')





    # add NAME and TITLE
    name = data.get('Name')[0]
    title = data.get('Name')[1]
    portrait = data.get('Images')[2]
    attack = data.get('Images')[5]
    special = data.get('Images')[8]
    injured = data.get('Images')[11]
    description = data.get('Description')
    rarity = data.get('Rarities')
    acquisition = data.get('Acquisition')
    blessing_type = None
    if data.get('Effect'):
        blessing_type = data.get('Effect')
    blessing_boost = None
    if data.get('Ally Boost'):
        blessing_boost = data.get('Ally Boost')
    duo_skill = None
    if data.get('Duo Skill'):
        duo_skill = data.get('Duo Skill')
    duel = None
    if data.get('Standard Effect 1: Duel'):
        duel = data.get('Standard Effect 1: Duel')     # TODO change key to just 'Duel'?
    pair_up = None
    if data.get('Standard Effect 2: Pair Up'):
        pair_up = data.get('Standard Effect 2: Pair Up')  # TODO change key to just 'Pair Up'?
    weapon_type = data.get('Weapon Type')
    move_type = data.get('Move Type')

    stats = data.get('Stats')
    char_hp = stats.get('HP')
    char_atk = stats.get('Atk')
    char_spd = stats.get('Spd')
    char_def = stats.get('Def')
    char_res = stats.get('Res')
    char_total = stats.get('Total')

    weapons = data.get('Weapons')

    assists = data.get('Assists')

    specials = data.get('Specials')

    passives = data.get('Passives')




    cursor.execute('''INSERT INTO Character_Images (portrait,
                                                    attack, 
                                                    special,
                                                    injured)
                                       VALUES (?, ?, ?, ?)''',
                                                   (portrait,
                                                    attack,
                                                    special,
                                                    injured))

    # var = image_id ''; image_id = 'select max(image_id) from character_images';

    image_id = cursor.lastrowid
    # print(image_id)


    # cursor.execute('''INSERT INTO Character_Stats (hp,
    #                                                atk,
    #                                                spd,
    #                                                def,
    #                                                res,
    #                                                total)
    #                         VALUES (?, ?, ?, ?, ?, ?)''',
    #                                               (char_hp,
    #                                                char_atk,
    #                                                char_spd,
    #                                                char_def,
    #                                                char_res,
    #                                                char_total))
    #
    # stats_id = cursor.lastrowid

    cursor.execute('''INSERT INTO Character (name, 
                                             title,
                                             image_id,
                                             description, 
                                             rarity, 
                                             acquisition, 
                                             blessing_type,
                                             blessing_boost,
                                             duo_skill,
                                             duel,
                                             pair_up, 
                                             weapon_type, 
                                             move_type,
                                             hp, 
                                             atk, 
                                             spd, 
                                             def, 
                                             res, 
                                             total, 
                                             weapons,
                                             assists,
                                             specials,
                                             passives)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                            (name,
                                             title,
                                             image_id,
                                             description,
                                             rarity,
                                             acquisition,
                                             blessing_type,
                                             blessing_boost,
                                             duo_skill,
                                             duel,
                                             pair_up,
                                             weapon_type,
                                             move_type,
                                             char_hp,
                                             char_atk,
                                             char_spd,
                                             char_def,
                                             char_res,
                                             char_total,
                                             weapons,
                                             assists,
                                             specials,
                                             passives))






    connection.commit()
