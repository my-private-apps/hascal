/* Hascal Programming Language
   Hascal Standard Library v1.0
   conv.d >>> a interface for convert.has library
*/

import std.conv;
//----------------------
// Testing the library
// enter following command in yout terminal for test :
// dmd -run conv.d

// the main test code(before test remove the comments)
/*import std.stdio;
void main(){
	writeln("\n++++Testing to_float() function :");
	writeln(to_float("1.22"));
	writeln(to_float(1));
	writeln(to_float(true));
	writeln(to_float(1.22));
	
	writeln("\n++++Testing to_int() function :");
	writeln(to_int("122"));
	writeln(to_int(1));
	writeln(to_int(true));
	writeln(to_int(1.22));
	
	writeln("\n+++Testing to_string() function :");
	writeln(to_string("122"));
	writeln(to_string(1));
	writeln(to_string(true));
	writeln(to_string(1.22));
	
}*/
//----------------------




// convert types to int
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

// convert types to string
string to_string(int s){
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

// convert types to float
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