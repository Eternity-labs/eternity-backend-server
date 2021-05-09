# eternity_backend_server


## 运行 eternity_backend_server

**运行环境**

python3.7+

**运行 eternity_backend_server**

~~~bash
git clone https://github.com/Eternity-labs/eternity-backend-server.git

cd eternity_backend_server/

cp .envrc eternity_backend_server/.env

pip install -r requirements.txt

python manager.py init_db
# init db

python manager.py runserver 
# 运行服务
~~~
-----------------


~~~bash
positional arguments:
  {runserver,shell,reset_local_db,reset_server_db,reset_db,init_local_db,init_server_db,init_db,set_user}
    runserver           Runs the Flask development server i.e. app.run()
    shell               Runs a Python shell inside Flask application context.
    reset_local_db      Reset local databases.
    reset_server_db     Reset server databases.
    reset_db            Reset all databases.
    init_local_db       Initialized local databases.
    init_server_db      Initialized server databases.
    init_db             Initialized all databases.
    set_user            Add A New User.
~~~