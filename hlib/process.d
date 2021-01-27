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