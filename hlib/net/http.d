/* Hascal Programming Language
   Hascal Standard Library v1.0
   http.d >>> a interface for net/http.has library
*/

import std.net.curl;

//----------------------
// Testing the library
// enter following command in yout terminal for test :
// dmd -run conv.d

// the main test code(before test remove the comments)
/*
void main(){
    download("http://google.com/", "google");
    auto content = get("https://httpbin.org/get");   
    auto content1 = post("https://httpbin.org/post", ["name1" : "value1", "name2" : "value2"]);
    auto content2 = post("https://httpbin.org/post", [1,2,3,4]);
    foreach (line; byLine("https://example.com/"))
        writeln(line);
}
*/
