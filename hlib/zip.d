import std.zip;
import std.file ;
import std.string : representation;


void CreateZipFromFile(string file_name,string file_data,string output){
	try {
		ArchiveMember file = new ArchiveMember();
		file.name = file_name;
		file.expandedData(file_data.dup.representation);
		file.compressionMethod = CompressionMethod.none;
	
		ZipArchive zip = new ZipArchive();
		zip.addMember(file);
		void[] compressed_data = zip.build();
		std.file.write(output,compressed_data);
	}catch (Exception e){
		writeln("Runtime Error : cannot create zip file ");
	}
}
