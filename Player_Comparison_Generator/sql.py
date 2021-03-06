import sqlite3
from scipy import spatial

conn = sqlite3.connect('player_comps.db')
c = conn.cursor()

def create_tables():
    c.execute('DROP TABLE IF EXISTS per40_comps')
    c.execute('''CREATE TABLE IF NOT EXISTS per40_comps
        (name TEXT,
        height TEXT,
        weight INTEGER,
        season TEXT,
        school TEXT,
        conf TEXT,
        gp INTEGER,
        mp INTEGER,
        fg NUMERIC,
        fga NUMERIC,
        fgp NUMERIC,
        two_p NUMERIC,
        two_pa NUMERIC,
        two_pp NUMERIC,
        three_p NUMERIC,
        three_pa NUMERIC,
        three_pp NUMERIC,
        ft NUMERIC,
        fta NUMERIC,
        ftp NUMERIC,
        trb NUMERIC,
        ast NUMERIC,
        stl NUMERIC,
        blk NUMERIC,
        pts NUMERIC,
        status TEXT)''') #nba player or prospect
    #c.execute('CREATE TABLE IF NOT EXISTS advanced_comps(name TEXT, per REAL)')

def data_entry():
    #---------------------2005 NBA Draft w/ other notable players--------------------
    c.execute('INSERT INTO per40_comps VALUES("Andrew Bogut","7-0",245,"2003-04","Utah","MWC",33,1002,6.7,11.6,.577,6.5,11.2,.586,0.2,0.4,.364,2.8,4.4,.640,13.0,2.9,0.6,1.8,16.4,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Andrew Bogut","7-0",245,"2004-05","Utah","MWC",35,1224,9.2,14.8,.620,8.9,14.0,.636,0.3,0.8,.360,4.7,6.8,.692,14.0,2.7,1.1,2.1,23.4,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Marvin Williams","6-9",230,"2004-05","UNC","ACC",36,800,6.3,12.4,.506,5.3,10.2,.522,1.0,2.2,.432,6.9,8.2,.847,11.8,1.3,2.0,0.9,20.4,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Deron Williams","6-3",210,"2002-03","Illinois","Big Ten",32,868,3.5,8.1,.426,2.2,4.5,.485,1.3,3.6,.354,1.1,2.1,.533,4.4,6.7,2.1,0.2,9.3,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Deron Williams","6-3",210,"2003-04","Illinois","Big Ten",30,1017,5.8,14.2,.408,3.1,7.5,.421,2.6,6.7,.394,2.3,2.9,.787,3.8,7.3,1.2,0.4,16.5,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Deron Williams","6-3",210,"2004-05","Illinois","Big Ten",39,1315,5.4,12.5,.433,3.3,6.8,.491,2.1,5.7,.364,2.0,2.9,.677,4.3,8.0,1.2,0.2,14.9,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Chris Paul","6-0",175,"2003-04","Wake Forest","ACC",31,1041,5.2,10.5,.496,3.7,7.1,.511,1.5,3.3,.465,5.8,6.8,.843,3.9,7.0,3.2,0.5,17.7,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Chris Paul","6-0",175,"2004-05","Wake Forest","ACC",32,1069,5.4,11.9,.451,3.6,8.2,.441,1.7,3.6,.474,5.8,7.0,.834,5.4,7.9,2.8,0.0,18.3,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Raymond Felton","6-1",198,"2002-03","UNC","ACC",35,1240,4.9,12.2,.398,2.6,6.0,.441,2.2,6.2,.358,2.5,3.7,.693,4.6,7.6,1.8,0.3,14.5,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Raymond Felton","6-1",198,"2003-04","UNC","ACC",30,1039,4.4,10.4,.420,3.0,6.0,.497,1.3,4.3,.313,3.3,4.0,.810,4.6,8.2,2.5,0.3,13.3,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Raymond Felton","6-1",198,"2004-05","UNC","ACC",36,1142,5.3,11.6,.455,2.8,6.0,.468,2.5,5.6,.440,3.3,4.7,.701,5.4,8.7,2.5,0.4,16.3,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Charlie Villanueva","6-11",240,"2003-04","UConn","Big East",32,607,7.4,14.5,.514,6.3,11.3,.556,1.2,3.2,.367,2.8,4.2,.667,11.1,1.5,0.4,3.2,18.8,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Charlie Villanueva","6-11",240,"2004-05","UConn","Big East",31,798,8.0,15.3,.521,7.7,14.7,.522,0.3,0.6,.500,4.9,7.1,.688,12.9,2.0,1.0,2.9,21.1,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Channing Frye","6-11",248,"2001-02","Arizona","Pac-10",34,814,6.0,10.1,.595,6.0,10.1,.595,0.0,0.0,.000,3.9,5.4,.727,10.5,1.2,0.8,2.5,15.9,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Channing Frye","6-11",248,"2002-03","Arizona","Pac-10",32,814,8.1,14.3,.569,8.1,14.2,.571,0.0,0.0,.000,3.6,5.4,.664,12.6,1.1,0.9,2.9,19.8,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Channing Frye","6-11",248,"2003-04","Arizona","Pac-10",30,910,8.5,15.5,.548,8.4,15.3,.548,0.1,0.2,.600,3.9,5.0,.788,9.8,2.5,0.7,2.8,21.0,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Channing Frye","6-11",248,"2004-05","Arizona","Pac-10",37,1148,7.9,14.3,.554,7.8,13.7,.570,0.1,0.6,.176,4.4,5.3,.830,9.8,2.5,1.2,3.0,20.3,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Ike Diogu","6-8",250,"2002-03","Arizona State","Pac-10",32,1030,8.1,13.4,.608,7.8,12.4,.625,0.3,0.9,.375,7.0,9.5,.735,9.7,1.0,0.3,1.2,23.6,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Ike Diogu","6-8",250,"2003-04","Arizona State","Pac-10",27,996,7.2,13.6,.530,6.6,12.1,.548,0.6,1.5,.378,9.8,12.0,.815,9.7,1.8,0.5,1.9,24.7,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Ike Diogu","6-8",250,"2004-05","Arizona State","Pac-10",32,1164,7.9,13.7,.575,7.3,12.1,.598,0.6,1.5,.400,8.5,10.7,.797,10.7,1.5,0.6,2.6,24.9,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Sean May","6-9",266,"2002-03","UNC","ACC",11,308,6.6,14.0,.472,6.6,13.5,.490,0.0,0.5,.000,3.0,5.2,.575,11.6,1.4,2.2,2.6,16.2,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Sean May","6-9",266,"2003-04","UNC","ACC",29,839,7.8,16.8,.463,7.8,16.6,.468,0.0,0.2,.000,5.5,8.0,.689,13.6,1.9,1.9,1.7,21.0,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Sean May","6-9",266,"2004-005","UNC","ACC",37,992,9.2,16.2,.567,9.2,16.1,.571,0.0,0.1,.000,7.7,10.2,.758,16.0,2.5,1.7,1.5,26.1,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Rashad McCants","6-4",207,"2002-03","UNC","ACC",35,1046,8.2,16.7,.491,5.5,10.1,.542,2.8,6.7,.414,3.5,5.0,.697,6.2,2.0,1.9,0.7,22.7,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Rashad McCants","6-4",207,"2003-04","UNC","ACC",30,961,9.0,18.8,.479,5.7,10.8,.531,3.2,8.0,.408,3.7,5.0,.748,5.7,2.7,2.2,0.8,24.9,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Rashad McCants","6-4",207,"2004-05","UNC","ACC",33,856,8.6,17.5,.489,5.2,9.6,.544,3.3,7.9,.423,4.3,5.9,.722,4.6,4.1,2.0,1.0,24.7,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Antoine Wright","6-7",210,"2002-03","Texas A&M","Big 12",28,889,6.5,17.8,.364,3.6,10.4,.351,2.8,7.4,.382,2.5,4.0,.611,8.4,2.2,1.6,0.9,18.3,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Antoine Wright","6-7",210,"2003-04","Texas A&M","Big 12",28,852,6.1,16.6,.368,3.9,9.2,.426,2.2,7.4,.297,3.4,5.4,.626,5.4,3.1,1.1,0.4,17.8,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Antoine Wright","6-7",210,"2004-05","Texas A&M","Big 12",31,1052,7.3,14.6,.501,4.6,8.6,.540,2.7,6.0,.447,3.7,5.3,.691,7.0,2.6,1.4,0.8,21.0,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Joey Graham","6-7",225,"2000-01","UCF","A-Sun",31,632,5.8,12.2,.474,5.1,8.9,.571,0.7,3.3,.212,4.4,5.2,.841,7.4,2.1,1.7,0.4,16.6,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Joey Graham","6-7",225,"2001-02","UCF","A-Sun",29,832,6.4,12.6,.510,5.5,10.1,.540,1.0,2.5,.385,4.7,6.2,.766,7.8,3.4,1.0,0.7,18.6,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Joey Graham","6-7",225,"2001-02","Oklahoma State","Big 12",35,864,7.9,13.8,.576,7.3,12.4,.586,0.6,1.3,.483,3.6,5.1,.709,8.5,1.9,1.1,0.3,20.1,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Joey Graham","6-7",225,"2001-02","Oklahoma State","Big 12",33,1009,8.0,15.1,.529,6.9,12.9,.538,1.0,2.2,.473,6.2,7.0,.887,8.1,2.7,1.2,0.2,23.2,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Danny Granger","6-8",225,"2001-02","Bradley","MVC",29,712,6.2,14.0,.446,6.1,13.0,.466,0.2,1.0,.176,5.5,7.0,.790,11.6,1.2,2.1,3.9,18.1,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Danny Granger","6-8",225,"2002-03","Bradley","MVC",14,380,10.4,20.1,.518,9.8,18.0,.544,0.6,2.1,.300,6.8,10.0,.684,11.7,1.7,2.0,2.0,28.3,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Danny Granger","6-8",225,"2003-04","New Mexico","MWC",22,703,7.7,15.8,.491,6.4,11.7,.546,1.4,4.1,.333,7.6,10.0,.760,11.2,2.6,1.7,1.8,24.4,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Danny Granger","6-8",225,"2004-05","New Mexico","MWC",30,900,8.1,15.5,.524,6.1,10.9,.563,2.0,4.6,.433,6.8,9.1,.755,11.8,3.2,2.8,2.7,25.1,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Hakim Warrick","6-9",219,"2001-02","Syracuse","Big East",35,609,6.2,11.3,.552,6.2,11.2,.553,0.1,0.1,.500,1.5,3.9,.383,11.0,1.2,1.3,1.4,14.1,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Hakim Warrick","6-9",219,"2001-02","Syracuse","Big East",35,1146,6.9,12.7,.541,6.9,12.7,.543,0.0,0.0,.000,4.3,6.5,.667,10.4,2.0,1.7,1.5,18.1,"nba")')
    c.execute('INSERT INTO per40_comps VALUES("Hakim Warrick","6-9",219,"2001-02","Syracuse","Big East",31,1156,7.7,15.0,.512,7.7,14.8,.519,0.0,0.2,.000,5.9,8.5,.692,9.2,2.8,1.0,1.2,21.3,"prospect")')
    c.execute('INSERT INTO per40_comps VALUES("Hakim Warrick","6-9",219,"2001-02","Syracuse","Big East",34,1275,7.9,14.5,.548,7.7,13.5,.566,0.3,1.0,.290,6.6,9.7,.681,9.2,1.6,1.0,0.8,22.8,"prospect")')




    conn.commit()
    #c.execute('INSERT INTO advanced_comps VALUES("Andrew Bogut", 7.1)')
    #conn.commit()
    #c.close()
    #conn.close()

class Player:
    __name = ""
    __height = 0
    __weight = 0
    __season = ""
    __school = ""
    __conf = ""
    __gp = 0
    __mp = 0
    __fg = 0
    __fga = 0
    __fgp = 0
    __two_p = 0
    __two_pa = 0
    __two_pp = 0
    __three_p = 0
    __three_pa = 0
    __three_pp = 0
    __ft = 0
    __fta = 0
    __ftp = 0
    __trb = 0
    __ast = 0
    __stl = 0
    __blk = 0
    __pts = 0
    __status = ""
    __compare_list = []

    def __init__(self, name, height, weight, season, school, conf, gp, mp, fg, fga, fgp, two_p, two_pa, two_pp, three_p, three_pa, three_pp, ft, fta, ftp, trb, ast, stl, blk, pts, status):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__season = season
        self.__school = school
        self.__conf = conf
        self.__gp = gp
        self.__mp = mp
        self.__fg = fg
        self.__fga = fga
        self.__fgp = fgp
        self.__two_p = two_p
        self.__two_pa = two_pa
        self.__two_pp = two_pp
        self.__three_p = three_p
        self.__three_pa = three_pa
        self.__three_pp = three_pp
        self.__ft = ft
        self.__fta = fta
        self.__ftp = ftp
        self.__trb = trb
        self.__ast = ast
        self.__stl = stl
        self.__blk = blk
        self.__pts = pts
        self.__status = status
        self.__compare_list = []

    def print_player(self):
        print(self.__name, self.__season, self.__pts, self.__status)

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_season(self):
        return self.__season

    def get_school(self):
        return self.__school

    def get_conf(self):
        return self.__conf

    def get_gp(self):
        return self.__gp

    def get_mp(self):
        return self.__mp

    def get_fg(self):
        return self.__fg

    def get_fga(self):
        return self.__fga

    def get_fgp(self):
        return self.__fgp

    def get_two_p(self):
        return self.__two_p

    def get_two_pa(self):
        return self.__two_pa

    def get_two_pp(self):
        return self.__two_pp

    def get_three_p(self):
        return self.__three_p

    def get_three_pa(self):
        return self.__three_pa

    def get_three_pp(self):
        return self.__three_pp

    def get_ft(self):
        return self.__ft

    def get_fta(self):
        return self.__fta

    def get_ftp(self):
        return self.__ftp

    def get_trb(self):
        return self.__trb

    def get_ast(self):
        return self.__ast

    def  get_stl(self):
        return self.__stl

    def get_blk(self):
        return self.__blk

    def get_pts(self):
        return self.__pts

    def get_status(self):
        return self.__status

    def compare(self, nba_player):
        for n in nba_player:
            dog = self.single_comparison(n)
            self.__compare_list.append(dog)
        return None

    def single_comparison(self, n):
        prospect_data = [self.get_fg(),self.get_fga(),self.get_fgp()*100]
        nba_player_data = [n.get_fg(),n.get_fga(),n.get_fgp()*100]
        sim_score = 1 - spatial.distance.cosine(prospect_data, nba_player_data)
        print(prospect_data)
        print(nba_player_data)
        print(sim_score)
        return sim_score

    def get_compare(self):
        return self.__compare_list


def read_from_db():
    c.execute('SELECT * FROM per40_comps')
    nba_list = []
    prospect_list = []
    for row in c.fetchall():
        cat = Player(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24], row[25])
        if cat.get_status() == "nba":
            nba_list.append(cat)
        else:
            prospect_list.append(cat)
    return nba_list, prospect_list

def printDB():
    try:
        result = c.execute('SELECT * FROM per40_comps')
        for row in result:
            print('Name: ', row[0], 'Height: ', row[1], 'Weight: ', row[2], 'Season: ', row[3], 'School: ', row[4],
                  'Conference: ', row[5], 'Games: ', row[6], 'Minutes: ', row[7], 'FG: ', row[8],
                  'FGA: ', row[9], 'FG%: ', row[10], '2P: ', row[11], '2PA: ', row[12], '2P%: ', row[13],
                  '3P: ', row[14], '3PA: ', row[15], '3P%: ', row[16], 'FT: ', row[17], 'FTA: ', row[18],
                  'FT%: ', row[19], 'TRB: ', row[20], 'AST: ', row[21], 'STL: ', row[22], 'BLK: ', row[23],
                  'PTS: ', row[24]
                  )

    except sqlite3.OperationalError:
        print "Error printing the DB"

create_tables()
data_entry()
nba_list, prospect_list = read_from_db()

for a in nba_list: #each element is a class Player
    a.print_player()


for p in prospect_list:
    p.compare(nba_list)

for j in prospect_list:
    j.print_player()
    comparisons = j.get_compare()
    i = 0
    for c in comparisons:
        print("player is ", nba_list[i].get_name(), " similarity: ", c)
        #print("player is ", i , " similarity: ", c)
        i = i + 1
exit()


print("prospect is ", players[prospect].get_name())
i = 0
for p in players:
    print("player is ", p.get_name(), " similarity: ", compare_list[i])
    i = i + 1


#printDB()

#c.close()
#conn.close()