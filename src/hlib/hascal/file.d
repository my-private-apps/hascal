import std.file;

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


