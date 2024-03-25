#!/usr/bin/pup
# scrit that install package 
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
