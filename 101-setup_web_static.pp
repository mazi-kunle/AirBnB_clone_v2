# A puppet manifest

exec {'update_apt'
  command => 'sudo apt-get -y update',
  path    => '/usr/bin'
}

exec {'install nginx'
  command => 'sudo apt-get -y install nginx',
  path    => '/usr/bin'
}

exec {'create_dir'
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell
}

exec {'create_dir2'
  command  => 'sudo mkdir /data/web_static/shared/',
  provider => shell
}

file {'/data/web_static/releases/test/index.html'
  ensure  => present,
  content => '<html>\n<body>\nHolberton School\n</body>\n</html>'
}

exec {'create_sym'
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell
}

exec {'config'
  command  => 'sudo sed -i "29 a\	location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default',
  provider => shell
}

exec {'chown'
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  provider => shell
}

exec {'nginx_restart'
  command  => 'sudo service nginx restart',
  provider => shell
}
