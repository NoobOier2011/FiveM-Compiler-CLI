import structlog
import os
import sys

logger = structlog.get_logger()
log = logger.bind(script="fivem_compiler_setup")

# what the fuck about windows dir system?!
download_dir = "./"
running_dir = '.\\'

logger.info("Ciallo~ (∠・ω< )⌒★")

logger.info("Be sure you install Visual Studio ", Workloads = ''' .NET desktop development, Desktop development with C++, Windows application development'''
,Individual_components = ''' .NET Framework 4.6 targeting pack, Windows 11 SDK (10.0.22000.0)''')

logger.info("download directory", path = download_dir)

logger.info("Your Arch? 'x86_64' or 'i686'")
Arch = input()

logger.info("Your CPU's job? (must be int)")
try:
  job = int(input())
except:
  logger.error("Check your answer!")
  sys.exit(0)

if (Arch != "x86_64" and Arch != "i686"):
  logger.error("Check your answer!")
  sys.exit(0)

command = [
    # Env
    {
        "download": 'curl -O --output-dir "' + download_dir + '" "' + "http://mirrors.tuna.tsinghua.edu.cn/msys2/distrib/msys2-" + Arch + "-latest.exe" + '"',
        "description": "msys2 installer",
        "install": os.path.join(running_dir, "msys2-" + Arch + "-latest.exe")
    },
    {
        "download": 'curl -O --output-dir "' + download_dir + '" "' + "https://mirrors.tuna.tsinghua.edu.cn/python/3.9.0/python-3.9.0.exe" + '"',
        "description": "Python 3.9.0",
        "install": os.path.join(running_dir, "python-3.9.0.exe")
    },
    {
        "download": 'curl -O --output-dir "' + download_dir + '" "' + "https://mirrors.tuna.tsinghua.edu.cn/github-release/git-for-windows/git/Git%20for%20Windows%20v2.51.2.windows.1/Git-2.51.2-64-bit.exe" + '"',
        "description": "Git",
        "install": os.path.join(running_dir, "Git-2.51.2-64-bit.exe")
    },
    {
        "download": 'curl -O --output-dir "' + download_dir + '" "' + "https://npmmirror.com/mirrors/node/v24.11.0/node-v24.11.0-x64.msi" + '"',
        "description": "Node.js",
        "install": os.path.join(running_dir, "node-v24.11.0-x64.msi")
    },
    {
        "download": None,
        "description": "setuptools",
        "install": "pip install setuptools"
    },
    {
        "download": None,
        "description": "Yarn",
        "install": "npm install -g yarn"
    }
]

for i in command:
    if i["download"] is not None:
        os.system(i["download"])
        logger.info(i["description"] + " is downloaded now!")
    os.system(i["install"])
    logger.info(i["description"] + " installer is running now!")

logger.info("Environment is OK now!")

logger.info("Start FiveM! compile? (y/n)")
answer = input()
if answer != "n":
    logger.info("Bye~ (・ω・)ノ")
    sys.exit(0)

logger.info("what do you want to compile? (server/client(five)/rdr3)")
answer = input()
if answer != "server" and answer != "client" and answer != "fivem" and answer != "rdr3":
    logger.error("Check your answer!")
    sys.exit(0)

logger.info("Compile FiveM! now")
os.system(running_dir + "\script\Complier.cmd")
os.system("fxd gen -game " + answer)
os.system("fxd vs -game " + answer)
logger.info("All done! Ciallo~ (∠・ω< )⌒★")