#  Puppet manifest that 
#	- install and configure an Nginx server 
#	- perform a 301 redirect when querying /redirect_me.

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':

  ensure => installed,

  require => Exec['update system']
}

file_line { 'install':

  ensure => 'present',

  path   => '/etc/nginx/sites-enabled/default',

  after  => 'listen 80 default_server;',

  line   => 'rewrite ^/redirect_me https://www.github.com/a-idk permanent;',
}

file { '/var/www/html/index.html':

  content => 'Hello World!',
}

service { 'nginx':

  ensure  => running,

  require => Package['nginx'],
}
