submit: *.cpp *.hpp replace.py
	cat ./answer.cpp | py replace.py | CLIP

run: build
	./answer.exe
	
build: *.cpp *.hpp
	g++ answer.cpp -o answer.exe