
import std.stdio;


import std.json;


 






int main(string[] args){
  
auto json_file = File("db.json" , "r");

auto myjson = "";

json_file.readf("%s" , myjson);

JSONValue j;

j = parseJSON(myjson);

writeln(j["name"].str);

return 0;}