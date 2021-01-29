import std.conv;
import core.stdc.stdio;
import std.string : strip;
import core.stdc.stdlib : exit ;
string ReadStr(){
	string tmp;
	tmp = readln();
	tmp.length = tmp.length - 1 ; // remove new line in end of string
	return tmp;
}

int ReadInt(){
	try{
		string tmp;
		tmp = readln();
		return to_int(strip(tmp));
	}catch(Exception e){
		writeln("Runtime Error : entered value are invalid");
	}
	return 0;
}

float ReadFloat(){
	string tmp;
	tmp = readln();
	return to_float(strip(tmp));
}


int to_int(string s){
	return to!int(s);
}
int to_int(float s){
	return to!int(s);
}
int to_int(bool s){
	return to!int(s);
}
int to_int(int s){
	return to!int(s);
}

string to_string(int s){
	return to!string(s);
}
string to_string(char s){
	return to!string(s);
}
string to_string(string s){
	return to!string(s);
}
string to_string(float s){
	return to!string(s);
}
string to_string(bool s){
	return to!string(s);
}
string to_string(char * s){
	return to!string(s);
}

float to_float(int s){
	return to!float(s);
}
float to_float(string s){
	return to!float(s);
}
float to_float(float s){
	return to!float(s);
}
float to_float(bool s){
	return to!float(s);
}
