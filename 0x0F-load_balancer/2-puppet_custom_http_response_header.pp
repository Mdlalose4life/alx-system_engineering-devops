#using puppet to install nginx and set it up
exec {'/usr/bin/env sudo apt-get update':}
-> package { 'nginx':
  ensure => installed,
}
-> file { '/var/www/html/index.html':
  content => 'Hello World',
}
-> file_line {
  ensure => present,
  path => '/etc/nginx/sites-available/default',
  line => "\tadd_header X-served-By ${hostname}",
  after => 'server_name_'
}
-> service{'nginx':
  ensure => running,
}
