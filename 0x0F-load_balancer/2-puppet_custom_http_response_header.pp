# Puppet to configure custom HTTP header response
#
# update ubuntu server
exec { 'update':
  command => '/usr/bin/apt-get -y update',
}
->
# install nginx web server on server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# custom Nginx response header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# start service
service { 'nginx':
ensure  => 'running',
enable  => true,
require => Package['nginx']
}
