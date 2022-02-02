# GNU Make configuration for MD-to-PDF using Pandoc

PDF = hpc_jargon.pdf

all: $(PDF)
.PHONY: all clean

%.pdf: %.md beamer.tex
	pandoc -f markdown+smart -t beamer --template beamer.tex $< -o $@

clean:
	rm -rv $(PDF)
