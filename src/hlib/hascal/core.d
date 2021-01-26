import std.conv;
import core.stdc.stdio;
void ReadStr(string x){
	/*string tmp;
	tmp = readln();
	return tmp;*/
	x = readln();
}

int ReadInt(){
	int tmp;
	readf!" %d"(tmp);
	return tmp;
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
