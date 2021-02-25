/* Hascal Runtime System and Standard Functions written in D
 * this file is a part of Hascal compiler
*/

import std.conv : to;
import std.stdio ;
import std.string ;
import core.stdc.stdlib : exit ;
import std.file;
import std.net.curl;
import std.math : sin,cos,tan,PI,fmax,fmin,abs;
import std.datetime.systime;
import std.process : executeShell,execute ,wait ;
import std.array : split;

string ReadStr(){
	try {
		string tmp;
		tmp = readln();
		tmp.length = tmp.length - 1 ;
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
	}
	catch(Exception e){
		writeln("Runtime Error : cannot convert type 'int' to type 'int',input data are invalid");
	}
	return 0;
}

string to_string(int s){
	try {
		return to!string(s);
	}
	catch(Exception e){
		writeln("Runtime Error : cannot convert type 'int' to type 'string',input data are invalid");
	}
	return "";
}

string to_string(char s){
	try {
		return to!string(s);
	}
	catch(Exception e){
		writeln("Runtime Error : cannot convert type 'char' to type 'string',input data are invalid");
	}
	return "";
}

string to_string(string s){
	try {
		return to!string(s);
	}
	catch(Exception e){
		writeln("Runtime Error : cannot convert type 'string' to type 'string',input data are invalid");
	}
	return "";
}

string to_string(float s){
	try {
		return to!string(s);
	}
	catch(Exception e){
		writeln("Runtime Error : cannot convert type 'float' to type 'string',input data are invalid");
	}
	return "";
}

string to_string(bool s){
	try {return to!string(s);}
	catch(Exception e){writeln("Runtime Error : cannot convert type 'bool' to type 'string',input data are invalid");}
	return "";
}

string to_string(char * s){
	try {return to!string(s);}
	catch(Exception e){writeln("Runtime Error : cannot convert type 'char *' to type 'string',input data are invalid");}
	return "";
}

float to_float(int s){
	try {return to!float(s);}
	catch(Exception e){writeln("Runtime Error : cannot convert type 'int' to type 'float',input data are invalid");}
	return 0.0;
}

float to_float(string s){
	try {return to!float(s);}
	catch(Exception e){writeln("Runtime Error : cannot convert type 'string' to type 'float',input data are invalid");}
	return 0.0;
}

float to_float(float s){
	try {return to!float(s);}
	catch(Exception e){writeln("Runtime Error : cannot convert type 'float' to type 'float',input data are invalid");}
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

void RemoveFile(string s){
	try {
		std.file.remove(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot remove '",s,"' file");
	}
}

string ReadFromFile(string file_name){
	try{
		string tmp;
		auto f = File(file_name,"r");
		f.readf!"%s"(tmp);
		return tmp;
	}catch(Exception e){
		writeln("Runtime Error : cannot read '",file_name,"' file.");
	}
	return "";
}

void WriteToFile(File myfile,string s){
	try {
		myfile.write(s);
	}catch(Exception e){
		writeln("Runtime Error : cannot write to '",myfile.name,"'.");
	}
}

void CloseFile(File myfile){
	try {
		myfile.close;
	}catch(Exception e){
		writeln("Runtime Error : cannot close '",myfile.name,"' file.");
	}
}

int GetYear(){

	try {
		SysTime today = Clock.currTime();
		return today.year;
	}catch(Exception e){
		writeln("Runtime Error : GetYear() function crashed");
	}
	return 0 ;
}

int GetMonth(){
	try {
		SysTime today = Clock.currTime();
		return today.month;
	}catch(Exception e){
		writeln("Runtime Error : GetMonth() function crashed");
	}
	return 0 ;
}

int GetDay(){
	try {
		SysTime today = Clock.currTime();
		return today.day;
	}catch(Exception e){
		writeln("Runtime Error : GetDay() function crashed");
	}
	return 0 ;
}

int GetHour(){
	try {
		SysTime today = Clock.currTime();
		return today.hour;
	}catch(Exception e){
		writeln("Runtime Error : GetHour() function crashed");
	}
	return 0 ;
}

int GetMinute(){
	try {
		SysTime today = Clock.currTime();
		return today.minute;
	}catch(Exception e){
		writeln("Runtime Error : GetMinute() function crashed");
	}
	return 0 ;
}

int GetSecond(){
	try {
		SysTime today = Clock.currTime();
		return today.second;
	}catch(Exception e){
		writeln("Runtime Error : GetSecond() function crashed");
	}
	return 0 ;
}

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