#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/


sudo rm -f /data/web_Static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

echo "<h1>simple content</h1>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo chown -hR "$USER":"$USER" /data/

string_to_replace="# pass PHP scripts to FastCGI server"
conf="location \/hbnb_static \{\n\t\talias \/data\/web_static\/current\/;\n\t\}\n\n\t# pass PHP scripts to FastCGI server"
path="/etc/nginx/sites-enabled/default"

sudo sed -i "s/$string_to_replace/$conf/" "$path"

sudo service nginx restart
exit 0
