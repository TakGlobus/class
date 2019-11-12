##### Assert Simulator
set ns [new Simulator]

#### Hyper-Parameter for Homework
# Rate at CBR:  Mbits  at bottleneck
set bandwidth 8

# Variant of TCP
set tcp_agent1 Reno
set tcp_agent2 Reno

##### Set Output Files
set file [open out_${bandwidth}Mb.tr w]
$ns trace-all $file
set namfile [open out_${bandwidth}Mb.nam w]
$ns namtrace-all $namfile
set tcpfile1 [open out_${bandwidth}Mb_1.tcp w]
Agent/TCP set trace_all_oneline_ true
set tcpfile5 [open out_${bandwidth}Mb_5.tcp w]
Agent/TCP set trace_all_oneline_ true

##### Set Nodes
set n1 [$ns node] 
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]

##### Set Links
$ns duplex-link $n1 $n2 10Mb 10ms DropTail
$ns duplex-link $n5 $n2 10Mb 10ms DropTail
$ns duplex-link $n2 $n3 10Mb 50ms DropTail
$ns duplex-link $n3 $n4 10Mb 10ms DropTail
$ns duplex-link $n6 $n3 10Mb 10ms DropTail
$ns duplex-link-op $n1 $n2 orient right-down
$ns duplex-link-op $n5 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n6 $n3 orient left-up
$ns duplex-link-op $n4 $n3 orient left-down
$ns duplex-link-op $n2 $n3 queuePos 0.5
#$ns duplex-link-op $n3 $n2 queuePos 0.5

##### Set Length of queue
$ns queue-limit $n2 $n3 7  
# original 20
$ns queue-limit $n3 $n2 7  

##### Set TCP Agent
# transmit band width 0.1Mbits
set tcp1 [new Agent/TCP/${tcp_agent1}]
$tcp1 set window_ 100
$tcp1 set packetSize_ 960
$ns attach-agent $n1 $tcp1
set sink4 [new Agent/TCPSink]
$ns attach-agent $n4 $sink4
$ns connect $tcp1 $sink4
$tcp1 set fid_ 0
$ns color 0 red

set tcp5 [new Agent/TCP/${tcp_agent2}]
$tcp5 set window_ 100
$tcp5 set packetSize_ 960
$ns attach-agent $n5 $tcp5
set sink6 [new Agent/TCPSink]
$ns attach-agent $n6 $sink6
$ns connect $tcp5 $sink6
$tcp5 set fid_ 1
$ns color 1 blue

### Set Output file for TCP Agent
$tcp1 attach-trace $tcpfile1
$tcp1 trace cwnd_
$tcp5 attach-trace $tcpfile5
$tcp5 trace cwnd_

##### Set FTP Applicatoin
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp5

#### Set UDP Agent
set udp1 [new Agent/UDP]
$ns attach-agent $n2 $udp1
set null [new Agent/Null]
$ns attach-agent $n3 $null
$ns connect $udp1 $null
$udp1 set fid_ 2
$ns color 2 green

##### Set CBR Applicatoin
set cbr1 [new Application/Traffic/CBR]
$cbr1 set packetSize_ 960
$cbr1 set rate_ ${bandwidth}mb
# Bandwidth: 1 packes/0.001 sec ==> 1.0 x 10^3 bytes ==> 8.0 x 10^3 bits/sec
#  K Mbits == > X x 8x10^3 bits ==> (X x 8 x10^3) x 10^-6Mbits
#  X ==> K/(8 x 10^-3)  
$cbr1 attach-agent $udp1


##### Scheduling
$ns at 0.0 "$cbr1 start"
$ns at 0.1 "$ftp1 start"
$ns at 0.2 "$ftp2 start"
$ns at 20.0 "$cbr1 stop"
$ns at 20.5 "$ftp1 stop"
$ns at 20.5 "$ftp2 stop"
$ns at 21.0 "finish"
proc finish {} {
  global ns file namfile tcpfile1 tcpfile5
  $ns flush-trace
  close $file
  close $namfile
  close $tcpfile1
  close $tcpfile5
  exit 0
}

##### Run!
$ns run

