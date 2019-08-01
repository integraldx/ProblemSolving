submit: *.cpp replace.py
	cat ./answer.cpp | py replace.py | CLIP

run: build
	./answer.exe
	
build: *.cpp
	g++ answer.cpp -o answer.exe