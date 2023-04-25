# Execute a command with pkill that will kill a process with exec
exec { 'pkill killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
