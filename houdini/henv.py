import subprocess
import os
import sys


class HoudiniEnvironment:

    def __init__(self, HFS: str) -> None:
        self._hfs = HFS
        self._cwd = os.getcwd()

    def run_command(self, command: str, command_args: list = []):
        #  /bin/bash -c 'pushd /opt/sesi/hfs19.5.303 && source houdini_setup && sesictrl print-license'
        _args = ' '.join(command_args)
        _cmd = 'pushd {HFS} && source houdini_setup && {cmd} {args}'.format(
            HFS=self._hfs, cmd=command, args=_args)
        cmd = ['/bin/bash', '-c', _cmd]
        process = subprocess.run(cmd,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(process.stdout.decode())
        print(process.stderr.decode())

    def run_script(self, script_file: str, script_args: list):
        # nyue@head0:/opt/sesi/hfs19.5.303$ (pushd /opt/sesi/hfs19.5.303 && source houdini_setup && sesictrl print-license)
        pass


def main(HFS: str):
    h = HoudiniEnvironment(HFS=HFS)
    h.run_command(command='sesictrl', command_args=['print-license'])


if __name__ == '__main__':
    HFS = sys.argv[1]
    main(HFS)
