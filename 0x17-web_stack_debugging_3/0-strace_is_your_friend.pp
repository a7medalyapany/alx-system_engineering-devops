# Puppet manifest to fix Apache 500 Internal Server Error

# Fix file permissions
file { '/var/www/html':
  ensure  => 'directory',
  recurse => 'true',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

# Restart Apache service
service { 'apache2':
  ensure  => 'running',
  enable  => 'true',
  require => File['/var/www/html'],
}
