[app]

# 应用基本信息
title = ATSC钱包
package.name = atscwallet
package.domain = org.atsc.client

# 版本号
version = 10.12
version.release = 10.12

# 应用描述
description = ATSC区块链客户端钱包
author = ATSC Team

# 源代码目录
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json
source.exclude_exts = spec
source.exclude_dirs = tests, bin, .git, __pycache__, .buildozer

# Android平台配置 - 使用NDK 25b（满足最低版本要求）
android.archs = arm64-v8a
android.api = 30
android.minapi = 21
android.ndk = 25b
android.sdk = 30

# 应用权限
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# Python依赖库 - 锁定所有版本
requirements = python3==3.9.7,kivy==2.1.0,requests==2.31.0,websocket-client==1.5.1,pillow==10.1.0,cython==0.29.36

# 日志级别
log_level = 2

# 屏幕方向
orientation = portrait

# 全屏模式
fullscreen = 0

# AndroidX支持
android.enable_androidx = True

# 自动接受SDK许可证
android.accept_sdk_license = True

# 强制使用特定NDK版本
android.ndk_version = 25b
