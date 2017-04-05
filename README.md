# memtrack
track memory of process

## Synopsis

Memtrack tool gathers memory information about a process (extracted from procfs) and allow
to display them in different ways

Once started, you can type commands at the '$' prompt

## Motivation

Main motivation was education and understanding of the different memory info
avaiable in a scatter fashion in /proc

## Installation

Requires python

Run as root (sudo) to parse pagemap

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
 Mp <area id> [offset] [count]- display pages from selected area
     area id : id of area (from the list of areas)
     offset : offset in area (multiple of PAGE_SIZE)
     count : number of pages (can overlap next area)

A - address queries
 Ai <address> - display info about pages and memarea related
     to the provided address
Q - Quit
$
```

## Contributors

py06 (pkerbrat(at] free dot fr)

## License

GPLv3
