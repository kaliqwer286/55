[app]

# 应用基本信息
title = ATSC钱包
package.name = atscwallet
package.domain = org.atsc.client

# 应用版本
version = 10.12
version.release = 10.12

# 描述和作者
description = ATSC区块链客户端钱包 - 支持转账、商城、聊天功能
author = ATSC Team

# 源代码文件
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json
source.exclude_exts = spec
source.exclude_dirs = tests, bin, .git, __pycache__, .buildozer

# 应用图标（需要添加图标文件）
icon.filename = %(source.dir)s/icon.png

# 应用启动文件
presplash.filename = %(source.dir)s/splash.png

# 支持的架构
android.archs = arm64-v8a, armeabi-v7a

# Android SDK和NDK版本
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 33

# 应用权限
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# 应用主题
android.gradle_dependencies = 'androidx.appcompat:appcompat:1.6.1'

# 应用元数据
android.meta_data = 

# 添加Python库依赖
requirements = python3==3.9.7, kivy==2.1.0, requests==2.31.0, websocket-client==1.6.4, pillow==10.1.0

# 日志级别
log_level = 2

# Android权限
android.whitelist = 

# 应用服务
services.whitelist = 

# 允许外部存储
android.write_external_storage = True
android.read_external_storage = True

# 忽略依赖冲突
android.skip_update = False
android.add_src = 

# 应用签名（调试用）
android.release_artifact = False

# 应用取向
orientation = portrait

# 全屏模式
fullscreen = 0

# 窗口大小（仅桌面调试用）
window.size = 360x640

# Kivy设置
kivy_requirements = kivy
osx.python_version = 3
osx.kivy_version = 2.1.0

# iOS设置（忽略）
ios.codesign.debug = 
ios.codesign.release = 
ios.info_plist = 

# 其他设置
presplash.footer = false
presplash.filename = %(source.dir)s/presplash.png