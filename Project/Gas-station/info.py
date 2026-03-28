from db import infos
from config import *

def create_info(id):
    if infos.find_one({
        'id' : id
    }):
        return
    infos.insert_one({
        'id' : id,
        'day' : 1,
        'rating' : 0,
        'money' : 1000,
        'today_num' : 0,
        'total_num' : 0,
        'diesel_tank' : 100,
        'gasoline_tank' : 100,
        'electric_battery' : 100,
        'hydrogen_tank' : 100, 
        'nuclear_reactor' : 100,
        'diesel_price' : 10,
        'gasoline_price' : 15,
        'electricity_price' : 20,
        'hydrogen_price' : 25,
        'nuclear_price' : 30
    })

def adj_rating(id, adj):
    infos.update_one({
        'id' : id
    }, {
        '$inc': {
            'rating': adj
        }
    })

def adj_tank(id, option, change):
    infos.update_one({
        'id' : id
    }, {
        '$inc' : {
            option : change
        }
    })
    
def pass_day(id):
    infos.update_one({
        'id' : id
    }, {
        '$inc' : {
            'day' : 1
        },
        '$set' : {
            'today_num' : 0
        }
    })

'''
TODO
투데이 넘 토탈 넘 바꿔야 함
'''
def inc_consumer(id, cl_num):
    infos.update_one({
        'id' : id
    }, {
        '$inc' : {
            'today_num' : cl_num,
            'total_num' : cl_num
        }
    })

def adj_price(id, option, multiply):
    infos.update_one({
        'id' : id
    }, {
        '$inc' : {
            option : multiply
        }
    })

def adj_money(id, income):
    infos.update_one({
        'id' : id
    }, {
        '$inc' : {
            'money' : income
        }
    })
    
def load_info(id, key):
    key1 = infos.find_one({
        'id' : id
    }, {
        key : 1
    })[key]
    return key1
