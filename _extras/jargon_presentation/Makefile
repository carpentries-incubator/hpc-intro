# GNU Make configuration for MD-to-PDF using Pandoc

PDF = hpc_jargon.pdf

all: $(PDF)
.PHONY: all clean

%.pdf: %.md
	pandoc -f markdown -t beamer $< -o $@

clean:
	rm -rv $(PDF)
