# Fix for optimizing Nginx performance

exec { 'fix--for-nginx':
  command     => 'sed -i "s/sendfile on/sendfile off/" /etc/nginx/nginx.conf',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['fix--for-nginx'],
}
