import subprocess
import os


class HoudiniEnvironment:

    def __init__(self, HFS: str) -> None:
        self._hfs = HFS
        self._cwd = os.getcwd()

    def run_command(self, command: str, command_args: str = ''):
        #  /bin/bash -c 'pushd /opt/sesi/hfs19.5.303 && source houdini_setup && sesictrl print-license'
        _cmd = 'pushd {HFS} && source houdini_setup && {cmd} {args}'.format(
            HFS=self._hfs, cmd=command, args=command_args)
        cmd = ['/bin/bash', '-c', _cmd]
        process = subprocess.run(cmd,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(process.stdout.decode())
        print(process.stderr.decode())

    def run_script(self, script_file: str, script_args: list):
        # nyue@head0:/opt/sesi/hfs19.5.303$ (pushd /opt/sesi/hfs19.5.303 && source houdini_setup && sesictrl print-license)
        pass


def main():
    h = HoudiniEnvironment(HFS='/opt/sesi/hfs19.5.303')
    h.run_command(command='sesictrl', command_args='print-license')


if __name__ == '__main__':
    main()
