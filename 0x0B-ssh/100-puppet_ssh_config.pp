# Creates a file with puppet

file_line {
'passAuth':
ensure  => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no'
;
'KeyLocation':
ensure  => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/school'
}

