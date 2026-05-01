[app]

# 应用基本信息
title = ATSC钱包
package.name = atscwallet
package.domain = org.atsc.client

# 版本号
version = 10.12
version.release = 10.12

# 应用描述
description = ATSC区块链客户端钱包 - 支持转账、商城、聊天功能
author = ATSC Team

# 源代码目录
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json
source.exclude_exts = spec
source.exclude_dirs = tests, bin, .git, __pycache__, .buildozer

# 图标文件（可选，如果没有可以删除这行）
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splash.png

# Android平台配置
android.archs = arm64-v8a, armeabi-v7a
android.api = 30
android.minapi = 21
android.ndk = 25b
android.sdk = 30

# 应用权限
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Python依赖库
requirements = python3,kivy==2.1.0,requests==2.31.0,websocket-client==1.5.1,pillow==10.1.0

# 日志级别
log_level = 2

# 屏幕方向
orientation = portrait

# 全屏模式（0=不全屏，1=全屏）
fullscreen = 0

# AndroidX支持
android.enable_androidx = True

# Gradle依赖
android.gradle_dependencies = 'androidx.appcompat:appcompat:1.3.1'

# 自动接受SDK许可证
android.accept_sdk_license = True

# 其他设置
android.skip_update = False
