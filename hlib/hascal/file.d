import std.file;

void RemoveFile(string s){
	std.file.remove(s);
}
string ReadFromFile(string file_name){
	string tmp;
	auto f = File(file_name,"r");
	f.readf!"%s"(tmp);
	return tmp;
	
}


