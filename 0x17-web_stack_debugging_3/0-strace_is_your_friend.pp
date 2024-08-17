# Puppet code to fix the Apache 500 error, changing phpp to php

exec { 'fixing the phpp issue':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
