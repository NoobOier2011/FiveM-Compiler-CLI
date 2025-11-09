# FiveM-Compiler-CLI

An automated script to prepare the environment and compile FiveM, originally contributed by [NoobOier2011 (SaoNian)](https://github.com/NoobOier2011) and [Xiaoha](https://github.com/xiaoha-6).

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
    <a href="https://github.com/NoobOier2011/FiveM-Compiler-CLI/issues">Report a bug</a>
    ·
    <a href="https://github.com/NoobOier2011/FiveM-Compiler-CLI/issues">Request a feature</a>
  </p>
</p>

## Features

- Automatically download and run common dependency installers (msys2, Python, Git, Node.js, etc.)
- Install Python setuptools and global yarn
- Run the build script that fetches FiveM sources and triggers the build (script/Complier.cmd)
- Interactive CLI via cli.py to choose architecture and the number of parallel jobs

## Requirements

- Windows 10/11 (running installers as Administrator is recommended)
- Internet access to external mirrors (TUNA, npmmirror, GitHub, etc.)
- At least 4GB RAM and a multi-core CPU recommended (building is resource intensive)

## Quick Start

1. Clone or download this repository to your machine (assume you are at e:\Project\FiveM-Compiler-CLI).
2. Open PowerShell or CMD as Administrator and change to the project directory:
   - cd e:\Project\FiveM-Compiler-CLI
3. Run the preparation script:
   - python cli.py
   - Follow prompts to select target architecture (x86_64 or i686) and the number of parallel build jobs (integer).
4. cli.py will download and run required installers and then execute script\Complier.cmd, which pulls the FiveM source, updates submodules and starts the build.

Note: Some installers (msys2, Git, Node.js) may require manual completion of the installer UI or adding their executables to the system PATH after installation.

## Script Details

- cli.py
  - Prompts for architecture and job count, downloads standard installers and runs installation commands, then launches script\Complier.cmd.
- script\Complier.cmd
  - Clones the FiveM repository, initializes submodules, installs Python setuptools, downloads the correct Chrome version (fxd get-chrome), generates bindings and runs the fxd toolchain to build FiveM.

## Recommendations

- Run installation steps as Administrator (installers may write to Program Files and modify PATH).
- Ensure Git LFS and msys2 environment/dependencies are installed properly before building (refer to FiveM official docs).
- If a step fails, inspect the terminal output and fix the reported issue (common causes: missing dependencies, network timeouts).

## Contributing

Contributions are welcome. Please open an Issue or submit a Pull Request and include a brief description of changes and reproduction steps.

## License

Follow the license information provided by upstream projects and this repository. Add or consult a LICENSE file in the repo if needed.

## Acknowledgements

- FiveM / citizenfx community and authors for their source and build tools
- Mirror providers (TUNA, npmmirror) for download acceleration
- All contributors to this project