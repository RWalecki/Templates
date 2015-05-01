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

	open build/${PROJECT}.pdf
	open /Applications/iTerm.app
clean:
	rm -rf build/*
