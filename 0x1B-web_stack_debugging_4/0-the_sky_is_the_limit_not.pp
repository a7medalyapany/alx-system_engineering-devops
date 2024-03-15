# Fix for optimizing Nginx performance

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => file('/etc/nginx/nginx.conf'),
  replace => 'on',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  notify  => Service['nginx'],
}

exec { 'fix--for-nginx':
  command     => 'sed -i "s/sendfile on/sendfile off/" /etc/nginx/nginx.conf',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
}
