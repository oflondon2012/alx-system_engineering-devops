# Puppet to configure custom HTTP header response

# Get the server update
exec { 'update_server':
  command => '/usr/bin/apt-get -y update',
}

#install nginx now
package { 'ngix':
  ensure => 'installed',
}

# ensure the service is running
service { 'nginx':
  ensure => 'running',
  enable => 'true',
  require => Package['nginx'],
}

# create hellow world in the server root
file_world { '/var/www/html/index.html' :
  content => 'Hello World!',
}

# customise response header for nginx

file { 'nginx_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
  require => Service['nginx'],
}
