
import std.stdio;


import std.conv;
import core.stdc.stdio;
import std.string : strip;
string ReadStr(){
	string tmp;
	tmp = readln();
	return strip(tmp);
}

int ReadInt(){
	string tmp;
	tmp = readln();
	return to_int(strip(tmp));
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


 





import std.process : executeShell,execute ,wait ;
import std.array : split;
void ShellCommand(string com){
	try {
		auto prc = executeShell(com);
		if (prc.status != 0){
			writeln("Runtime Error : cannot excute command");
		}else {
			writeln(prc.output);
		}
	}catch(Exception e) {
		writeln("Runtime Error : cannot excute command");
	}
}

void ExcuteCommand(string com){
auto comm = com.split(" ");
	if(com == null){
		writeln("Runtime Error : command cannot empty");
		goto exit;
	}
	
	if(comm[0] == null){
		writeln("Runtime Error : command cannot empty");
		goto exit;
	}
	try {
	auto prc = execute(comm);
		writeln(prc.output);
	}catch(Exception e){
		writeln("Runtime error : cannot excute command");
	}
exit:
		auto tmp = 0;
		tmp++;
	
}

 






int main(string[] args){
  
auto comm = "";

while(true){
write(">>>");

comm = ReadStr();

ExcuteCommand(comm);
}

return 0;}