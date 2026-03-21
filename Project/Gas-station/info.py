from db import infos

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
        'rating' : {'$inc' : adj}
    })

def adj_tank(id, option, change):
    if option == 'd':
        infos.update_one({
            'id' : id
        }, {
            'diesel_tank' : {'$inc' : change}
        })
    elif option == 'g':
        infos.update_one({
            'id' : id
        }, {
            'gasoline_tank' : {'$inc' : change}
        })
    
    elif option == 'e':
        infos.update_one({
            'id' : id
        }, {
            'electric_battery' : {'$inc' : change}
        })
    
    elif option == 'h':
        infos.update_one({
            'id' : id
        }, {
            'hydrogen_tank' : {'$inc' : change}
        })
    
    elif option == 'n':
        infos.update_one({
            'id' : id
        }, {
            'nuclear_reactor' : {'$inc' : change}
        })
    
def pass_day(id):
    infos.update_one({
        'id' : id
    }, {
        'day' : {'$inc' : 1},
        '$set' : {
            'today_num' : 0
        }
    })
def inc_consumer(id, cl_num):
    infos.update_one({
        'id' : id
    }, {
        'today_num' : {'$inc' : cl_num},
        'total_num' : {'$inc' : cl_num}
    })
def adj_money(id, income):
    infos.update_one({
        'id' : id
    }, {
        'money' : {'$inc' : income}
    })
def load_info(id, key):
    key1 = infos.find_one({
        'id' : id
    }, {
        key : 1
    })[key]
    return key1
