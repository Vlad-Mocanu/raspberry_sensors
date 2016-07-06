#!/usr/bin/python
import MySQLdb
import os
import glob
import time
import thread
import RPi.GPIO as io
io.setmode(io.BCM)

#create table windows (id int not null auto_increment, name varchar(30), state int, date timestamp, primary key (id));

class Window:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        io.setup(self.pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp
        self.update_state()

    def get_current_state(self):
        return io.input(self.pin)

    def update_state(self):
        self.state = self.get_current_state()

    def get_sql(self):
        return "insert into sensors.windows (name, state, date) values(\"" + self.name + "\", " + str(self.state) + ", NOW());"

class Temperature:
    def __init__(self, device_file):
        self.device_file = device_file

    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

    def get_sql(self):
        return "insert into sensors.temperature (value, date) values(" + str(round(self.read_temp(), 4)) + ", NOW());"


def write_to_db(my_sql):
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="123",        # your password
                         db="sensors")        # name of the data base

    # you must create a Cursor object. It will let you execute all the queries you need
    cursor = db.cursor()
    
    try:
        # Execute the SQL command and commit changes in the database 
        cursor.execute(my_sql)
        db.commit()
    except:
        db.rollback()

    # disconnect from server
    db.close()

def window_thread():
    #initialization for windows
    all_windows = []
    all_windows.append(Window("Living LEFT", 23))
    all_windows.append(Window("Living RIGHT", 24))

    for win in all_windows:
        sql = win.get_sql()
        print(sql)
        write_to_db(sql)

    while True:
        for win in all_windows:
            if (win.get_current_state() != win.state):
                win.update_state()
                sql = win.get_sql()
                print(sql)
                write_to_db(sql)

        time.sleep(10)

def temp_thread():
    #initialization for tempetature
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    temp = Temperature(device_folder + '/w1_slave')
        
    while True:
        sql = temp.get_sql()
        print(sql)
        write_to_db(sql)
        time.sleep(1800)

thread.start_new_thread(temp_thread, ())
thread.start_new_thread(window_thread, ())
while True:
    time.sleep(1800)
