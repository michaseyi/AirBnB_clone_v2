
$config="\
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.nginx-debian.html;
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}"

package { 'nginx':
    ensure => installed,
}

exec { 'mkdir -p /data/web_static/releases/test':
    provider => shell,
}

file { '/data/web_static/releases/test/index.html':
    ensure  => present,
    content => '/hbnb_static/index.html',
}

exec { 'mkdir -p /data/web_static/shared':
    provider => shell,
}

file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test'
}

exec { 'chown -R ubuntu:ubuntu /data':
    provider    => shell,
}

file { '/etc/nginx/sites-available/default':
    ensure  => 'present',
    content => $config,
}

exec { 'service nginx restart':
    provider => shell,
}
