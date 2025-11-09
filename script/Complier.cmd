git clone https://github.com/citizenfx/fivem.git -c core.symlinks=true
cd fivem
git submodule update --jobs=16 --init

:: if you're using Python 3.12 or higher make sure you install the setuptools package
pip install setuptools

:: downloads the right Chrome version for 64-bit projects
fxd get-chrome

:: build bindings of game natives.
prebuild

:: or -game server/-game rdr3
fxd gen -game five
fxd vs -game five