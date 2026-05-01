[app]

# 应用基本信息
title = ATSC钱包
package.name = atscwallet
package.domain = org.atsc.client

# 版本信息
version = 10.12
version.release = 10.12

# 描述和作者
description = ATSC区块链客户端钱包 - 支持转账、商城、聊天功能
author = ATSC Team

# 源代码设置
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json
source.exclude_exts = spec
source.exclude_dirs = tests, bin, .git, __pycache__, .buildozer

# 应用图标（可选，如果没有可以注释掉）
# icon.filename = %(source.dir)s/icon.png

# 启动画面（只保留一行，不要重复）
presplash.filename = %(source.dir)s/splash.png

# 支持的架构
android.archs = arm64-v8a, armeabi-v7a

# Android SDK和NDK版本
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

# 应用权限
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# 依赖库 - 确保所有需要的库都在这里
requirements = python3,kivy==2.1.0,requests==2.31.0,websocket-client==1.6.4,pillow==10.1.0

# 日志级别
log_level = 2

# 应用取向
orientation = portrait

# 全屏模式
fullscreen = 0

# AndroidX支持
android.enable_androidx = True

# Gradle依赖
android.gradle_dependencies = 'androidx.appcompat:appcompat:1.3.1'

# 其他设置
android.whitelist = 
android.ignore_manifest = False
android.skip_update = False

# 调试设置
android.release_artifact = False
