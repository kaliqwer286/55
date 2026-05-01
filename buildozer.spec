[app]

title = ATSC Wallet
package.name = atscwallet
package.domain = org.atsc

version = 10.12
version.release = 10.12

description = ATSC Blockchain Wallet
author = ATSC

source.dir = .
source.include_exts = py

android.archs = arm64-v8a
android.api = 30
android.minapi = 21

android.permissions = INTERNET

requirements = python3,kivy,requests,websocket-client

orientation = portrait

android.accept_sdk_license = True
