##### Assert Simulator
set ns [new Simulator]

##### Set Output Files
set file [open out.tr w]
$ns trace-all $file
set namfile [open out.nam w]
$ns namtrace-all $namfile
set tcpfile [open out.tcp w]
Agent/TCP set trace_all_oneline_ true

##### Set Nodes
set n1 [$ns node] 
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]

##### Set Links
$ns duplex-link $n1 $n2 10Mb 5ms DropTail
$ns duplex-link $n5 $n2 10Mb 5ms DropTail
$ns duplex-link $n2 $n3 10Mb 10ms DropTail
$ns duplex-link $n3 $n4 10Mb 5ms DropTail
$ns duplex-link $n6 $n3 10Mb 5ms DropTail
$ns duplex-link-op $n1 $n2 orient right-down
$ns duplex-link-op $n5 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n6 $n3 orient left-up
$ns duplex-link-op $n4 $n3 orient left-down
$ns duplex-link-op $n2 $n3 queuePos 0.5
$ns duplex-link-op $n3 $n2 queuePos 0.5

##### Set Length of queue
$ns queue-limit $n2 $n3 20
$ns queue-limit $n3 $n2 20

##### Set UDP Agent
#set udp [new Agent/UDP]
#$ns attach-agent $n1 $udp
#set null [new Agent/Null]
#$ns attach-agent $n3 $null
#$ns connect $udp $null
#$udp set fid_ 0
#$ns color 0 blue

##### Set TCP Agent
set tcp1 [new Agent/TCP/Reno]
$ns attach-agent $n1 $tcp1
set sink4 [new Agent/TCPSink]
$ns attach-agent $n4 $sink4
$ns connect $tcp1 $sink4
$tcp1 set fid_ 0
$ns color 0 red

set tcp5 [new Agent/TCP/Reno]
$ns attach-agent $n5 $tcp5
set sink6 [new Agent/TCPSink]
$ns attach-agent $n6 $sink6
$ns connect $tcp5 $sink6
$tcp5 set fid_ 1
$ns color 1 blue

##### Set CBR Applicatoin
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $tcp1
set cbr2 [new Application/Traffic/CBR]
$cbr2 attach-agent $tcp5

### Set Output file for TCP Agent
$tcp1 attach-trace $tcpfile
$tcp1 trace cwnd_
$tcp5 attach-trace $tcpfile
$tcp5 trace cwnd_

##### Set FTP Application
set ftp [new Application/FTP]
$ftp attach-agent $tcp1
$ftp attach-agent $tcp5

##### Scheduling
$ns at 0.5 "$cbr1 start"
$ns at 1.0 "$cbr2 start"
$ns at 1.5 "$ftp start"
$ns at 3.0 "$ftp stop"
$ns at 3.5 "$cbr1 stop"
$ns at 4.0 "$cbr2 stop"
$ns at 4.5 "finish"
proc finish {} {
  global ns file namfile tcpfile
  $ns flush-trace
  close $file
  close $namfile
  close $tcpfile
  exit 0
}

##### Run!
$ns run

