#!/usr/bin/env bash
# puppet script to change my configuration file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#client configuration
	host*
	#specify the file name as ~/0-RSA_public_key instead
	IdentityFile ~/.ssh/school
	PasswordAuthentication no

}
