# FiveM-Compiler-CLI

A Auto Script to compile FiveM by [NoobOier2011(SaoNian)](https://github.com/NoobOier2011) and [Xiaoha](https://github.com/xiaoha-6)

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/NoobOier2011/FiveM-Compiler-CLI">
    <img src="icon.ico" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">FiveM-Compiler-CLI</h3>
  <p align="center">
    FiveM-Compiler-CLI
    <br />
    <br />
    <a href="https://github.com/NoobOier2011/FiveM-Compiler-CLI/issues">报告Bug</a>
    ·
    <a href="https://github.com/NoobOier2011/FiveM-Compiler-CLI/issues">提出新特性</a>
  </p>
</p>

## 功能

- 自动下载并执行常用依赖安装器（msys2、Python、Git、Node.js 等）
- 安装 Python setuptools 与全局 yarn
- 运行用于获取 FiveM 源码与生成/编译的批处理脚本（script/Complier.cmd）
- 通过 cli.py 提示交互，支持选择架构与并行作业数

## 要求

- Windows 10/11（以管理员权限运行安装器更稳妥）
- 网络访问外部镜像（TUNA、npmmirror、GitHub 等）
- 推荐至少 4GB 内存与多核 CPU（编译占用较高）

## 快速开始

1. 克隆或下载本仓库到本地（设你当前在 e:\Project\FiveM-Compiler-CLI）。
2. 以管理员身份打开 PowerShell 或 CMD，进入项目目录：
   - cd e:\Project\FiveM-Compiler-CLI
3. 运行准备脚本：
   - python cli.py
   - 按提示输入目标架构（x86_64 或 i686）和并行编译作业数（整数）。
4. cli.py 会下载并执行必要安装程序并运行 script\Complier.cmd，后者负责拉取 FiveM 源码、更新子模块并发起构建流程。

注意：某些安装器（例如 msys2、Git、Node.js）需要手动完成安装向导，或在安装后将可执行路径加入系统 PATH。

## 脚本说明

- cli.py
  - 提示用户输入架构与作业数，下载常用安装器并执行安装命令，最后触发 script\Complier.cmd。
- script\Complier.cmd
  - 克隆 FiveM 仓库、初始化子模块、安装 Python setuptools、下载 Chrome（fxd get-chrome）、生成绑定并运行 fxd 工具链以构建 FiveM。

## 使用建议

- 以管理员权限运行安装步骤（安装器需写入 Program Files、修改 PATH 等）。
- 编译前确保 Git LFS、msys2 的环境与依赖安装完毕（根据 fivem 官方文档）。
- 若某个步骤失败，查看终端输出并按提示修复（缺少依赖、网络超时等常见问题）。

## 贡献

欢迎提交 Issue 或 Pull Request。请在 PR 中简要描述更改与复现步骤。

## 许可证

根据上游项目及本仓库 README 中声明。

## 致谢

- FiveM / citizenfx 社区与作者提供的源代码与构建工具
- 镜像站点（如 TUNA、npmmirror）提供下载加速
- 本项目所有的开发者