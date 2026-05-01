# ATSC钱包 Android版 v10.12

ATSC区块链客户端钱包，支持转账、商城购物、区域管理、即时聊天等功能。

## 🚀 自动打包APK

本项目配置了GitHub Actions自动打包流程。

### 使用方法：

1. **Fork此仓库** 到你的GitHub账号

2. **触发打包**：
   - 方式一：推送代码到 `main` 分支自动触发
   - 方式二：在GitHub页面点击 `Actions` → `Build APK` → `Run workflow`

3. **下载APK**：
   - 等待15-30分钟
   - 进入 `Actions` 页面
   - 点击成功的工作流记录
   - 在 `Artifacts` 区域下载APK文件

## 📱 安装说明

1. 下载 `ATSC-Wallet-v10.12.apk`
2. 在手机上允许"安装未知应用"
3. 点击安装

## ⚙️ 首次使用配置

1. 打开App后，点击右上角 ⚙️ 设置按钮
2. 输入云服务器IP地址（默认127.0.0.1为本地测试）
3. 注册新账号或登录已有账号

## 🔧 手动本地打包（可选）

```bash
# 安装buildozer
pip install buildozer

# 初始化配置
buildozer init

# 打包APK
buildozer android debug deploy run