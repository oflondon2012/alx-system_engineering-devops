# Puppet to configure custom HTTP header response
#
# update ubuntu server
exec { 'update':
  command => '/usr/bin/apt-get -y update',
}
->
# install nginx now
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# customise response header for nginx
file_line { 'res_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# ensure the service is running
service { 'nginx':
ensure  => 'running',
enable  => true,
require => Package['nginx']
}
