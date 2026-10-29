[app]
title = MSSUMY GSM PRO
package.name = mssumygsmpro
package.domain = org.mssumy.gsm
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 6.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,USB_PERMISSION,USB_HOST

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
