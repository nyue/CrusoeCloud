import subprocess
import shutil
import hashlib
import requests
import sys
import os
sys.path.append(os.path.dirname(__file__))
import sidefx
import henv

# print('python SESI_CLIENT_SECRET_KEY = {}'.format(os.environ['SESI_CLIENT_SECRET_KEY']))
# print('python SESI_CLIENT_ID = {}'.format(os.environ['SESI_CLIENT_ID']))


if __name__ == '__main__':
    service = sidefx.service(
        access_token_url="https://www.sidefx.com/oauth2/application_token",
        client_id=os.environ['SESI_CLIENT_ID'],
        client_secret_key=os.environ['SESI_CLIENT_SECRET_KEY'],
        endpoint_url="https://www.sidefx.com/api/",
    )
    assert (service)

    target_version = '19.5'
    target_platform = 'linux'
    target_product = 'houdini'
    # Retrieve the daily builds list, if you want the latest production
    # you can skip this step
    releases_list = service.download.get_daily_builds_list(
        product=target_product,
        only_production=True,
        version=target_version,
        platform=target_platform)
    if False:
        for item in releases_list:
            print(item)

    # Retrieve the latest daily build available
    latest_release = service.download.get_daily_build_download(
        product=target_product,
        version=target_version,
        build=releases_list[0]['build'],
        platform=target_platform)
    print(latest_release)

    # Download the file
    local_filename = os.path.join('/tmp',latest_release['filename'])
    r = requests.get(latest_release['download_url'], stream=True)
    if r.status_code == 200:
        with open(local_filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception('Error downloading file!')

    # Verify the file checksum is matching
    file_hash = hashlib.md5()
    with open(local_filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            file_hash.update(chunk)
    if file_hash.hexdigest() != latest_release['hash']:
        raise Exception('Checksum does not match!')

    # Extract downloaded file
    cmd = ['tar','-xvf',local_filename]
    subprocess.run(cmd,cwd='/tmp')

    # Run the Houdini installer
    basename = latest_release['filename'].split('.tar.gz')[0]
    cmd = ['./houdini.install','--auto-install', '--accept-EULA', '2021-10-13']
    cwd = os.path.join('/tmp',basename)
    subprocess.run(cmd,cwd=cwd)

    # Setup licensing
    HFS = os.path.join('/opt','hfs{v}'.format(v=target_version))
    hserver_path = os.path.join(HFS,'houdini','hserver.ini')
    with open(hserver_path,'w') as fp:
        fp.write('APIKey = {url} {client_id} {client_secret}\n'.format(url='www.sidefx.com',client_id=os.environ['SESI_CLIENT_ID'],client_secret=os.environ['SESI_CLIENT_SECRET_KEY']))

    ## Start hserver
    h = henv.HoudiniEnvironment(HFS)
    h.run_command(command='hserver')
    h.run_command(command='hserver', command_args=['-S','"https://www.sidefx.com/license/sesinetd"'])
    h.run_command(command='sesictrl', command_args=['print-license'])
