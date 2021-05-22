  
from eternity_backend_server import create_app
from flask_script import Manager, Server, Shell
app = create_app()

banner = r"""

 ____       __                                      __
/\  _`\    /\ \__                            __    /\ \__
\ \ \L\_\  \ \ ,_\     __    _ __    ___    /\_\   \ \ ,_\   __  __
 \ \  _\L   \ \ \/   /'__`\ /\`'__\/' _ `\  \/\ \   \ \ \/  /\ \/\ \
  \ \ \L\ \  \ \ \_ /\  __/ \ \ \/ /\ \/\ \  \ \ \   \ \ \_ \ \ \_\ \
   \ \____/   \ \__\\ \____\ \ \_\ \ \_\ \_\  \ \_\   \ \__\ \/`____ \
    \/___/     \/__/ \/____/  \/_/  \/_/\/_/   \/_/    \/__/  `/___/> \
                                                                 /\___/
                                                                 \/__/

"""

manager = Manager(app)


def make_shell_context():
    return {
        "app": app,
    }

manager.add_command("runserver", Server(host="127.0.0.1", port=5000, use_debugger=True))
manager.add_command("shell", Shell(banner=banner, make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()
