PROJECT=main

bibtex=bibtex
pdflatex=pdflatex

BIBTEX=$(bibtex) build/main.aux
BUILDTEX=$(pdflatex) \
		 -halt-on-error \
		--output-directory build \
		-aux-directory=build \
		$(PROJECT).tex


all:
	$(BUILDTEX)
	bibtex build/main.aux
	$(BUILDTEX)
	$(BUILDTEX)

clean:
	rm -rf build/*
