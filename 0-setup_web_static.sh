#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

#sudo apt-get -y update
#sudo apt-get -y install nginx

make_dir() {
        if [ ! -d "$1" ]; then
                sudo mkdir -p "$1"
        fi
}

make_dir /data/web_static/shared/
make_dir /data/web_static/releases/test/

if [ -f /data/web_static/current ]; then

	sudo rm -f /data/web_Static/current
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current

fi

echo "<h1>simple content</h1>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo chown -hR "$USER":"$USER" /data/

string_to_replace="# pass PHP scripts to FastCGI server"
conf="location \/hbnb_Static \{\n\t\talias \/data\/web_static\/current\/;\n\t\}\n\n\t# pass PHP scripts to FastCGI server"
path="/etc/nginx/sites-enabled/default"

sudo sed -i "s/$string_to_replace/$conf/" "$path"

sudo service nginx restart

