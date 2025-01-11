import redis

if __name__ == '__main__':
    try:
        r = redis.Redis(host='localhost', port=6379, db=0, password='Sup1nf0') 
        if r.ping():
            print("Connexion réussie à Redis !")
            
        r.set('foo', 'bar')
        value = r.get('foo')
        print(f"La valeur de 'foo' est : {value.decode('utf-8')}") 

    except redis.AuthenticationError as auth_error:
        print("Erreur d'authentification à Redis :", auth_error)

    except redis.ConnectionError as conn_error:
        print("Erreur de connexion à Redis :", conn_error)

    except Exception as e:
        print("Erreur :", e)