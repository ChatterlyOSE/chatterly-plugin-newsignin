# chatterly advanced sign in plugin

Chatterly Sign In Plugin, designed for use with the Modtools plugins.

This plugin is completely backwards-compatible with reddit OSS.

## installation

First, install the python package:

    python ./setup.py develop

To enable the plugin, you will need to add it to the plugins line of your
reddit .ini file:

    plugins = auth

To build static files for production, run `make` in the main reddit repository.
It will detect, build, and merge in the plugin static files for deployment.
