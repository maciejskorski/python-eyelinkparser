#
#
# author: Teunis van Beelen
#
# email: teuniz@protonmail.com
#
#

CC = gcc
CFLAGS = -std=gnu11 -O2 -Wall -Wextra -Wshadow -Wformat-nonliteral -Wformat-security -Wtype-limits -Wfatal-errors
LDLIBS =

objects = edf2ascii.o
headers =

all: edf2ascii

edf2ascii:	$(objects)
	$(CC) $(objects) -o edf2ascii $(LDLIBS)

edf2ascii.o:	edf2ascii.c $(headers)
	$(CC) $(CFLAGS) -c edf2ascii.c -o edf2ascii.o

clean:
	$(RM) edf2ascii $(objects)
