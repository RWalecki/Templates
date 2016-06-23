PROJECT=main

bibtex=bibtex
pdflatex=pdflatex

BIBTEX=$(bibtex) build/$(PROJECT).aux
BUILDTEX=$(pdflatex) \
		-halt-on-error \
		--output-directory build \
		-aux-directory=build \
		$(PROJECT).tex


all:
	$(BUILDTEX)
	$(BIBTEX)
	$(BUILDTEX)
	$(BUILDTEX)

clean:
	rm -rf build/*
