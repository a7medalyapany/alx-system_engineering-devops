# Allow the holberton user to open files without encountering "Too many open files" errors

file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton soft nofile 4096\nholberton hard nofile 8192",
}

exec { 'reload-limits':
  command     => 'ulimit -n 8192',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}

exec { 'reload-session':
  command     => 'exec su - holberton',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}

exec { 'reload-profile':
  command     => 'exec su - holberton',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}
