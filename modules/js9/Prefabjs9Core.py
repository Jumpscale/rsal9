from js9 import j

app = j.tools.prefab._getBaseAppClass()


class Prefabjs9Core(app):
    NAME = 'js9'

    def install(self, reset=False, branch='master'):
        """
        j.tools.prefab.local.js9.js9Core.install()

        or from bash

        js9_prefab local 'js9.js9core.install(reset=1)'

        """
        if self.doneCheck("install", reset):
            return

        self.prefab.system.base.install()

        self.bashtools()

        self._base()

        self.prefab.runtimes.pip.doneSet("ensure")  # pip is installed in above

        self.logger.info("js9_install")
        self.core.run(
            "export JS9BRANCH=%s;ZInstall_host_js9" % branch, profile=True)

        self.prefab.runtimes.pip.install("Cython,asyncssh,numpy,tarantool")

        self.doneSet("install")

    def bashtools(self, reset=False):

        if self.doneCheck("bashtools", reset):
            return

        S = """
        echo "INSTALL BASHTOOLS"
        curl https://raw.githubusercontent.com/Jumpscale/bash/master/install.sh?$RANDOM > /tmp/install.sh        
        bash /tmp/install.sh
        """

        self.core.execute_bash(S)

        self.doneSet("bashtools")

    def _base(self, reset=False):

        if self.doneCheck("base", reset):
            return

        self.core.run("ZInstall_host_base", profile=True)

        self.doneSet("base")