#!/bin/bash

# Download the complete works of Shakespeare from Project Gutenburg

echo "Downloading Collected works of William Shakespeare..."
wget -q https://www.gutenberg.org/ebooks/100.txt.utf-8 -O book_s.txt
echo "Done"

echo ""
echo "Creating data set..."
rm -f -v data.1
for i in 1 2 3 4 5 6 7 8 9 10
do
	cat book_s.txt >> data.1
done
rm book_s.txt
echo "Done"
echo ""
echo "Shakespeare data set:"
ls -lh data.1

############################

echo ""
echo "Downloading Cantebury Tales, by Geoffrey Chaucer..."
wget -q https://www.gutenberg.org/ebooks/2383.txt.utf-8 -O book_c.txt
echo "Done"

echo ""
echo "Creating data set..."
rm -f -v data.2
for i in 1 2 3 4 5 6 7 8 9 10
do
	cat book_c.txt >> data.2
done
rm book_c.txt
echo "Done"
echo ""
echo "Chaucer data set:"
ls -lh data.2

############################

echo ""
echo "Downloading Moby Dick, by Herman Melville..."
wget -q https://www.gutenberg.org/ebooks/2701.txt.utf-8 -O book_m.txt
echo "Done"

echo ""
echo "Creating data set..."
rm -f -v data.3
for i in 1 2 3 4 5 6 7 8 9 10
do
	cat book_m.txt >> data.3
done
rm book_m.txt
echo "Done"
echo ""
echo "Moby Dick data set:"
ls -lh data.3

############################

echo ""
echo "Downloading Homers The Odyssey..."
wget -q https://www.gutenberg.org/ebooks/1727.txt.utf-8 -O book_h.txt
echo "Done"

echo ""
echo "Creating data set..."
rm -f -v data.4
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
	cat book_h.txt >> data.4
done
rm book_h.txt
echo "Done"
echo ""
echo "The Odyssey data set:"
ls -lh data.4

############################

echo ""
echo "Our complete data set to analyse:"
ls -lh data.*
echo ""
