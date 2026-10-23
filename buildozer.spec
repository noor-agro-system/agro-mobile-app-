[التطبيق]التطبيق]

# (str) عنوان طلبك
title = النظام الزراعي

# (str) اسم الحزمة
الحزمة.الاسم = agroapp

# (str) مجال الحزمة (مطلوب لتغليف Android / iOS)
package.domain = org.agro

# (str) شفرة المصدر حيث يعيش main.py
المصدر.dir = .

# (قائمة) ملفات المصدر لتضمينها (تترك فارغة لتشمل جميع الملفات)
المصدر.include_exts = py,png,jpg,kv,atlas

# (str) إصدار التطبيق (الطريقة 1)
الإصدار = 1.0

# (قائمة) متطلبات التطبيق
requirements = python3,kivy,sqlite3

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
التوجه = صورة.

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
