# myLogin for Chatterly

myLogin for Chatterly, formerly Chatterly Advanced Sign On
This plugin is completely backwards-compatible with reddit OSS.

This plugin introduces myLogin for Chatterly by adding three new login
endpoints, /auth/signup, /auth/signin, and /auth/recovery. It also disables the 
pre-existing login and registration pages.

## installation

First, install the python package:

    python ./setup.py develop

To enable the plugin, you will need to add it to the plugins line of your
reddit .ini file:

    plugins = auth

To build static files for production, run `make` in the main reddit repository.
It will detect, build, and merge in the plugin static files for deployment.
