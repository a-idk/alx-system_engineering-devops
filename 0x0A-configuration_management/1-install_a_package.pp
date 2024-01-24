##!/usr/bin/pup

# First: is python present
package { 'python3.8':
  ensure => present,
}
# Second: check "pip"
package { 'python3-pip':
  ensure => present,
}
# Third: install flask 2.1.0 from pip3 using Puppet
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
# Fourth: Werkzeug present
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
