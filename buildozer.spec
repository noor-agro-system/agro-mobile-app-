[app]

# (str) Title of your application
title = النظام الزراعي

# (str) Package name
package.name = agroapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.agro

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,sqlite3

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android build tools version to use
android.build_tools_version = 33.0.2
# (bool) Accept SDK license
android.accept_sdk_license = True
