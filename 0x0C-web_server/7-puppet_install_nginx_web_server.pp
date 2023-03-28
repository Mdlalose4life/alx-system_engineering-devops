# configure the file

package {
  'nginx':
  ensure => installed,
}

file {
  '/var/www/html/index.nginx-debian.html'
  content => 'Hello World',
}

file_line {'configure redirection':
  path => '/etc/nginx/sites-available/default',
  after => 'server_name _'
  line => "\n\tlocation /redirect_me{\n\treturn 301 https://www.youtube.com/watch?v=ceRM2b00Mf4; \n\t}\n",
}

service {'nginx':
  ensure => running
}