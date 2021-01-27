static import std.file;

void RemoveFile(string s){
	std.file.remove(s);
}
void mkdir(string s){
	std.file.mkdir(s);
}
void rmdir(string s){
	std.file.rmdir(s);
}

