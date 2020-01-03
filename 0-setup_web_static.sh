#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

# Install nginx web server:
# apt-get -y update && apt-get install -y nginx

# Create folders if don't exist:

sudo mkdir -p "/data/web_static/releases/"
sudo mkdir -p "/data/web_static/shared/"
sudo mkdir -p "/data/web_static/releases/test/"

# Create a fake HTML file:
sudo touch /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/current /data/web_static/releases/test/

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R $ubuntu:$ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
#variable="/data/web_static/current/ $hbnb_static;"
#sed -i "24i $variable" /etc/nginx/sites-available/default

# Restart nginx:
service nginx restart
