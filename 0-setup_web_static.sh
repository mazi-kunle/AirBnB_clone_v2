#!/usr/bin/env bash
# configure a web server for thr deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo chmod 755 /data/
sudo mkdir -p /data/web_static/releases/
sudo chmod 777 /data/web_static/
sudo chmod 755 /data/web_static/releases
sudo mkdir -p /data/web_static/shared/
sudo chmod 755 /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chmod 777 /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '29 a\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
