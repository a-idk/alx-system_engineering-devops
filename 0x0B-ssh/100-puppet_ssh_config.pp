#!/usr/bin/env bash
# using Puppet to make changes to our configuration file

file { '/etc/ssh/ssh_config':
 	ensure => present,

content =>"

	# SSH configuration file with the following requirements:
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
