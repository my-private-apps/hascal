
import std.stdio;



int main(string[] args){
  
auto comm = "";

while(true){
write(">>>");

comm = ReadStr();

ExcuteCommand(comm);
}

return 0;}