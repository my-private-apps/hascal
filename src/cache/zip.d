
import std.stdio;


import std.zip;
import std.file ;
import std.string : representation;


void CreateZipFromFile(string file_name,string file_data,string output){
	ArchiveMember file = new ArchiveMember();
	file.name = "test1.txt";
    file.expandedData(file_data.dup.representation);
    file.compressionMethod = CompressionMethod.none;
	
	ZipArchive zip = new ZipArchive();
	zip.addMember(file);
	void[] compressed_data = zip.build();
	std.file.write(output,compressed_data);
}

 





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




 






int main(string[] args){
  
auto myfile = File("readyforzip.txt" , "r");

CreateZipFromFile(myfile.name , ReadFromFile(myfile.name) , "out.zip");

return 0;}