import std.conv;
import core.stdc.stdio;
import std.string : strip;
import core.stdc.stdlib : exit ;
string ReadStr(){
	try {
		string tmp;
		tmp = readln();
		tmp.length = tmp.length - 1 ; // remove new line in end of string
		return tmp;
	}catch(Exception e) {
		writeln("Runtime Error : cannot read string");
	}
	return "";
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
	try {
		string tmp;
		tmp = readln();
		return to_float(strip(tmp));
	}catch(Exception e){
		writeln("Runtime Error : entered value are invalid");
	}
	return 0.0;
}


int to_int(string s){
	try {
		return to!int(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'string' to type 'int',input data are invalid");
	}
	return 0;
	
}
int to_int(float s){
	try {
		return to!int(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'float' to type 'int',input data are invalid");
	}
	return 0;
}
int to_int(bool s){
	try {
		return to!int(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'bool' to type 'int',input data are invalid");
	}
	return 0;
}
int to_int(int s){
	try {
		return to!int(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'int' to type 'int',input data are invalid");
	}
	return 0;
}

string to_string(int s){
	try {
		return to!string(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'int' to type 'string',input data are invalid");
	}
	return "";
}
string to_string(char s){
	try {
		return to!string(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'char' to type 'string',input data are invalid");
	}
	return "";
}
string to_string(string s){
	try {
		return to!string(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'string' to type 'string',input data are invalid");
	}
	return "";
}
string to_string(float s){
	try {
		return to!string(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'float' to type 'string',input data are invalid");
	}
	return "";
}
string to_string(bool s){
	try {
		return to!string(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'bool' to type 'string',input data are invalid");
	}
	return "";
}
string to_string(char * s){
	try {
		return to!string(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'char *' to type 'string',input data are invalid");
	}
	return "";
}


float to_float(int s){
	try {
		return to!float(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'int' to type 'float',input data are invalid");
	}
	return 0.0;
}
float to_float(string s){
	try {
		return to!float(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'string' to type 'float',input data are invalid");
	}
	return 0.0;
}
float to_float(float s){
	try {
		return to!float(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'float' to type 'float',input data are invalid");
	}
	return 0.0;
}
float to_float(bool s){
	try {
		return to!float(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot convert type 'bool' to type 'float',input data are invalid");
	}
	return 0.0;
}
