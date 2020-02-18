import os
from cloudmesh.common.util import banner

class Provider:

    def __init__(self, name):
        self.name = name

    # def launch(self):
    #     banner(f"launch {self.name}")
    #     os.system(f"multipass launch --name {self.name}")
    #     print('\n')

    def start(self):
        banner(f"start {self.name}")
        os.system(f"multipass start {self.name}")
        print('\n')

    def info(self):
        banner("info")
        os.system("multipass info --all")
        print('\n')

    def get(self):
        banner("get")
        os.system("multipass get client.gui.autostart")
        print('\n')

    def stop(self):
        banner("stop")
        os.system("multipass stop")
        print('\n')

    def delete(self, purge=False):
        banner("delete")
        os.system("multipass delete --all")
        print('\n')

    def list(self):
        banner("list")
        os.system("multipass list")
        print('\n')

    def recover(self):
        banner("recover")
        os.system("multipass recover --all")
        print('\n')

if __name__ == "__main__":
    p = Provider("cloudmesh")
    # p.launch()
    p.start()
    p.info()
    p.get()
    p.list()
    p.stop()
    p.delete()
    p.recover()
    p.list()
