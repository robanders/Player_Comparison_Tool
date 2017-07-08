import sqlite3

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
        pts NUMERIC)''')
    #c.execute('CREATE TABLE IF NOT EXISTS advanced_comps(name TEXT, per REAL)')

def data_entry():
    #---------------------2005 NBA Draft w/ other notable players--------------------
    c.execute('INSERT INTO per40_comps VALUES("Andrew Bogut","7-0",245,"2003-04","Utah","MWC",33,1002,6.7,11.6,.577,6.5,11.2,.586,0.2,0.4,.364,2.8,4.4,.640,13.0,2.9,0.6,1.8,16.4)')
    c.execute('INSERT INTO per40_comps VALUES("Andrew Bogut","7-0",245,"2004-05","Utah","MWC",35,1224,9.2,14.8,.620,8.9,14.0,.636,0.3,0.8,.360,4.7,6.8,.692,14.0,2.7,1.1,2.1,23.4)')
    c.execute('INSERT INTO per40_comps VALUES("Marvin Williams","6-9",230,"2004-05","UNC","ACC",36,800,6.3,12.4,.506,5.3,10.2,.522,1.0,2.2,.432,6.9,8.2,.847,11.8,1.3,2.0,0.9,20.4)')
    c.execute('INSERT INTO per40_comps VALUES("Deron Williams","6-3",210,"2002-03","Illinois","Big Ten",32,868,3.5,8.1,.426,2.2,4.5,.485,1.3,3.6,.354,1.1,2.1,.533,4.4,6.7,2.1,0.2,9.3)')
    c.execute('INSERT INTO per40_comps VALUES("Deron Williams","6-3",210,"2003-04","Illinois","Big Ten",30,1017,5.8,14.2,.408,3.1,7.5,.421,2.6,6.7,.394,2.3,2.9,.787,3.8,7.3,1.2,0.4,16.5)')
    c.execute('INSERT INTO per40_comps VALUES("Deron Williams","6-3",210,"2004-05","Illinois","Big Ten",39,1315,5.4,12.5,.433,3.3,6.8,.491,2.1,5.7,.364,2.0,2.9,.677,4.3,8.0,1.2,0.2,14.9)')
    c.execute('INSERT INTO per40_comps VALUES("Chris Paul","6-0",175,"2003-04","Wake Forest","ACC",31,1041,5.2,10.5,.496,3.7,7.1,.511,1.5,3.3,.465,5.8,6.8,.843,3.9,7.0,3.2,0.5,17.7)')
    c.execute('INSERT INTO per40_comps VALUES("Chris Paul","6-0",175,"2004-05","Wake Forest","ACC",32,1069,5.4,11.9,.451,3.6,8.2,.441,1.7,3.6,.474,5.8,7.0,.834,5.4,7.9,2.8,0.0,18.3)')
    c.execute('INSERT INTO per40_comps VALUES("Raymond Felton","6-1",198,"2002-03","UNC","ACC",35,1240,4.9,12.2,.398,2.6,6.0,.441,2.2,6.2,.358,2.5,3.7,.693,4.6,7.6,1.8,0.3,14.5)')
    c.execute('INSERT INTO per40_comps VALUES("Raymond Felton","6-1",198,"2003-04","UNC","ACC",30,1039,4.4,10.4,.420,3.0,6.0,.497,1.3,4.3,.313,3.3,4.0,.810,4.6,8.2,2.5,0.3,13.3)')
    c.execute('INSERT INTO per40_comps VALUES("Raymond Felton","6-1",198,"2004-05","UNC","ACC",36,1142,5.3,11.6,.455,2.8,6.0,.468,2.5,5.6,.440,3.3,4.7,.701,5.4,8.7,2.5,0.4,16.3)')
    c.execute('INSERT INTO per40_comps VALUES("Charlie Villanueva","6-11",240,"2003-04","UConn","Big East",32,607,7.4,14.5,.514,6.3,11.3,.556,1.2,3.2,.367,2.8,4.2,.667,11.1,1.5,0.4,3.2,18.8)')
    c.execute('INSERT INTO per40_comps VALUES("Charlie Villanueva","6-11",240,"2004-05","UConn","Big East",31,798,8.0,15.3,.521,7.7,14.7,.522,0.3,0.6,.500,4.9,7.1,.688,12.9,2.0,1.0,2.9,21.1)')
    c.execute('INSERT INTO per40_comps VALUES("Channing Frye","6-11",248,"2001-02","Arizona","Pac-10",34,814,6.0,10.1,.595,6.0,10.1,.595,0.0,0.0,.000,3.9,5.4,.727,10.5,1.2,0.8,2.5,15.9)')
    c.execute('INSERT INTO per40_comps VALUES("Channing Frye","6-11",248,"2002-03","Arizona","Pac-10",32,814,8.1,14.3,.569,8.1,14.2,.571,0.0,0.0,.000,3.6,5.4,.664,12.6,1.1,0.9,2.9,19.8)')
    c.execute('INSERT INTO per40_comps VALUES("Channing Frye","6-11",248,"2003-04","Arizona","Pac-10",30,910,8.5,15.5,.548,8.4,15.3,.548,0.1,0.2,.600,3.9,5.0,.788,9.8,2.5,0.7,2.8,21.0)')
    c.execute('INSERT INTO per40_comps VALUES("Channing Frye","6-11",248,"2004-05","Arizona","Pac-10",37,1148,7.9,14.3,.554,7.8,13.7,.570,0.1,0.6,.176,4.4,5.3,.830,9.8,2.5,1.2,3.0,20.3)')
    c.execute('INSERT INTO per40_comps VALUES("Ike Diogu","6-8",250,"2002-03","Arizona State","Pac-10",32,1030,8.1,13.4,.608,7.8,12.4,.625,0.3,0.9,.375,7.0,9.5,.735,9.7,1.0,0.3,1.2,23.6)')
    c.execute('INSERT INTO per40_comps VALUES("Ike Diogu","6-8",250,"2003-04","Arizona State","Pac-10",27,996,7.2,13.6,.530,6.6,12.1,.548,0.6,1.5,.378,9.8,12.0,.815,9.7,1.8,0.5,1.9,24.7)')
    c.execute('INSERT INTO per40_comps VALUES("Ike Diogu","6-8",250,"2004-05","Arizona State","Pac-10",32,1164,7.9,13.7,.575,7.3,12.1,.598,0.6,1.5,.400,8.5,10.7,.797,10.7,1.5,0.6,2.6,24.9)')
    c.execute('INSERT INTO per40_comps VALUES("Sean May","6-9",266,"2002-03","UNC","ACC",11,308,6.6,14.0,.472,6.6,13.5,.490,0.0,0.5,.000,3.0,5.2,.575,11.6,1.4,2.2,2.6,16.2)')
    c.execute('INSERT INTO per40_comps VALUES("Sean May","6-9",266,"2003-04","UNC","ACC",29,839,7.8,16.8,.463,7.8,16.6,.468,0.0,0.2,.000,5.5,8.0,.689,13.6,1.9,1.9,1.7,21.0)')
    c.execute('INSERT INTO per40_comps VALUES("Sean May","6-9",266,"2004-005","UNC","ACC",37,992,9.2,16.2,.567,9.2,16.1,.571,0.0,0.1,.000,7.7,10.2,.758,16.0,2.5,1.7,1.5,26.1)')
    c.execute('INSERT INTO per40_comps VALUES("Rashad McCants","6-4",207,"2002-03","UNC","ACC",35,1046,8.2,16.7,.491,5.5,10.1,.542,2.8,6.7,.414,3.5,5.0,.697,6.2,2.0,1.9,0.7,22.7)')
    c.execute('INSERT INTO per40_comps VALUES("Rashad McCants","6-4",207,"2003-04","UNC","ACC",30,961,9.0,18.8,.479,5.7,10.8,.531,3.2,8.0,.408,3.7,5.0,.748,5.7,2.7,2.2,0.8,24.9)')
    c.execute('INSERT INTO per40_comps VALUES("Rashad McCants","6-4",207,"2004-05","UNC","ACC",33,856,8.6,17.5,.489,5.2,9.6,.544,3.3,7.9,.423,4.3,5.9,.722,4.6,4.1,2.0,1.0,24.7)')
    c.execute('INSERT INTO per40_comps VALUES("Antoine Wright","6-7",210,"2002-03","Texas A&M","Big 12",28,889,6.5,17.8,.364,3.6,10.4,.351,2.8,7.4,.382,2.5,4.0,.611,8.4,2.2,1.6,0.9,18.3)')
    c.execute('INSERT INTO per40_comps VALUES("Antoine Wright","6-7",210,"2003-04","Texas A&M","Big 12",28,852,6.1,16.6,.368,3.9,9.2,.426,2.2,7.4,.297,3.4,5.4,.626,5.4,3.1,1.1,0.4,17.8)')
    c.execute('INSERT INTO per40_comps VALUES("Antoine Wright","6-7",210,"2004-05","Texas A&M","Big 12",31,1052,7.3,14.6,.501,4.6,8.6,.540,2.7,6.0,.447,3.7,5.3,.691,7.0,2.6,1.4,0.8,21.0)')
    c.execute('INSERT INTO per40_comps VALUES("Joey Graham","6-7",225,"2000-01","UCF","A-Sun",31,632,5.8,12.2,.474,5.1,8.9,.571,0.7,3.3,.212,4.4,5.2,.841,7.4,2.1,1.7,0.4,16.6)')
    c.execute('INSERT INTO per40_comps VALUES("Joey Graham","6-7",225,"2001-02","UCF","A-Sun",29,832,6.4,12.6,.510,5.5,10.1,.540,1.0,2.5,.385,4.7,6.2,.766,7.8,3.4,1.0,0.7,18.6)')
    c.execute('INSERT INTO per40_comps VALUES("Joey Graham","6-7",225,"2001-02","Oklahoma State","Big 12",35,864,7.9,13.8,.576,7.3,12.4,.586,0.6,1.3,.483,3.6,5.1,.709,8.5,1.9,1.1,0.3,20.1)')
    c.execute('INSERT INTO per40_comps VALUES("Joey Graham","6-7",225,"2001-02","Oklahoma State","Big 12",33,1009,8.0,15.1,.529,6.9,12.9,.538,1.0,2.2,.473,6.2,7.0,.887,8.1,2.7,1.2,0.2,23.2)')
    c.execute('INSERT INTO per40_comps VALUES("Danny Granger","6-8",225,"2001-02","Bradley","MVC",29,712,6.2,14.0,.446,6.1,13.0,.466,0.2,1.0,.176,5.5,7.0,.790,11.6,1.2,2.1,3.9,18.1)')
    c.execute('INSERT INTO per40_comps VALUES("Danny Granger","6-8",225,"2002-03","Bradley","MVC",14,380,10.4,20.1,.518,9.8,18.0,.544,0.6,2.1,.300,6.8,10.0,.684,11.7,1.7,2.0,2.0,28.3)')
    c.execute('INSERT INTO per40_comps VALUES("Danny Granger","6-8",225,"2003-04","New Mexico","MWC",22,703,7.7,15.8,.491,6.4,11.7,.546,1.4,4.1,.333,7.6,10.0,.760,11.2,2.6,1.7,1.8,24.4)')
    c.execute('INSERT INTO per40_comps VALUES("Danny Granger","6-8",225,"2004-05","New Mexico","MWC",30,900,8.1,15.5,.524,6.1,10.9,.563,2.0,4.6,.433,6.8,9.1,.755,11.8,3.2,2.8,2.7,25.1)')




    conn.commit()
    #c.execute('INSERT INTO advanced_comps VALUES("Andrew Bogut", 7.1)')
    #conn.commit()
    #c.close()
    #conn.close()

def read_from_db():
    c.execute('SELECT * FROM per40_comps')
    data_list = []
    for row in c.fetchall():
        data_list.append(row)
    return data_list


create_tables()
data_entry()
read_from_db()

#c.close()
#conn.close()