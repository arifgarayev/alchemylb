import os
import subprocess
import time


class Commands:

    # yango pkg name = ru.yandex.taxi

    @staticmethod
    def launch_app(uuid, android_pkg_name):

        # R58W204XQPM
        # adb -s R58W204XQPM shell monkey -p ru.yandex.taxi -c android.intent.category.LAUNCHER 1
        os.system(f"adb -s {uuid} shell monkey -p {android_pkg_name} -c android.intent.category.LAUNCHER 1")
        time.sleep(12)

    @staticmethod
    def kill_app(uuid, android_pkg_name):

        os.system(f"adb -s {uuid} shell am force-stop {android_pkg_name}")
        time.sleep(5)

        return Commands

    @staticmethod
    def release_port_adb(uuid):
        os.system(f"adb -s {uuid} forward --remove-all")
        time.sleep(2)
        return Commands


    @staticmethod
    def sigkill_appium_process(port):

        p = os.system(f"kill -9 $(lsof -i:{port})")
        time.sleep(2)

        return Commands

    @staticmethod
    def is_device_online(uuid):
        if 'device' not in subprocess.check_output(f"adb -s {uuid} devices", shell=True).decode():
            raise ConnectionError('Please connect a device')


    @staticmethod
    def clean_appium_pkgs(uuid):

        for pkg_name in ('io.appium.uiautomator2.server', 'io.appium.uiautomator2.server.test'\
                         'io.appium.unlock', 'io.appium.settings'):


            os.system(f'adb -s {uuid} uninstall {pkg_name}')
            time.sleep(1.5)

