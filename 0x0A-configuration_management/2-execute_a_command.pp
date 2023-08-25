# create a manifest that kills a file

exec { 'kill_file':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
