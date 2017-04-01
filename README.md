# memtrack
track memory of process

## Synopsis

Memtrack gather memory information about a process (extracted procfs) and allow
to display them in different ways

Once started, you can type commande at the '$' prompt

## Motivation

Main motivation was education and understanding of the different memory info
avaiable in a scatter fashion in /proc

## Installation

Requires python

## Help
```
Tracking memory usage of process <PID> 
Event: memareas changed

$ h
P - process info

L - List memory areas

M - Memory areas info
 Ml - list mapped files by process
 Mf <mapped filename> - list areas associated to mapped file
 Mp <area id> - display pages from selected area

Q - Quit
$
```

## Contributors

py06 (pkerbrat(at] free dot fr)

## License

GPLv3
