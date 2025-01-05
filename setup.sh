#! /bin/sh
pip3 install .
cp -n ./config/config.example ./config/config.yml
"${EDITOR:-nano}" ./config/config.yml
echo "Successfully installed and configured TS3Proxy. Start it using ts3proxy"
