# Puppet manifest to fix Apache 500 error
file { '/etc/apache2/sites-available/your_website.conf':
  ensure => file,
  source => 'puppet:///modules/your_module/your_website.conf',
  notify => Exec['restart_apache'],
}

exec { 'restart_apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
}
