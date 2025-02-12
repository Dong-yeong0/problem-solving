def solution(id_pw, db):
    id_input, pw_input = id_pw
    for id_db, pw_db in db:
        if id_db == id_input:
            if pw_db == pw_input:
                return 'login'
            else:
                return 'wrong pw'
    
    return 'fail'
        