##!/usr/bin/pup
# install flask 2.1.0 from pip3 using Puppet
#package {'flask':
#  ensure   => '2.1.0',
#  provider => 'pip'
#  require
#}

exec {'install flask':
  command => '/usr/bin/pip3 install flask==2.1.0'
}
