[app]

# (str) Title of your application
title = MSSUMY GSM PRO

# (str) Package name
package.name = mssumygsmpro

# (str) Package domain (needed for android packaging)
package.domain = org.mssumy.gsm

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Directory to load source files from
source.dir = .

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyusb

# (str) Supported orientations
orientation = portrait

# (int) Whether to be a fullscreen application
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,USB_PERMISSION,USB_HOST

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept Android SDK license
android.accept_sdk_license = True

# (list) The android archs to build for,, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
