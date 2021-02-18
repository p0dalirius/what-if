SRCDIR=./src
BINDIR=./bin

all : clean compile

clean :
	@rm -rf ${BINDIR}/*

compile :
	@if [ ! -d "${BINDIR}" ]; then mkdir -p ${BINDIR}; fi
	gcc -Wall ${SRCDIR}/main.c -O0 -o ${BINDIR}/infmalloc
