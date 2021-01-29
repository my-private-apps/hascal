import std.datetime.systime;

int GetYear(){
	SysTime today = Clock.currTime();
	return today.year;
}

int GetMonth(){
	SysTime today = Clock.currTime();
	return today.month;
}

int GetDay(){
	SysTime today = Clock.currTime();
	return today.day;
}

int GetHour(){
	SysTime today = Clock.currTime();
	return today.hour;
}

int GetMinute(){
	SysTime today = Clock.currTime();
	return today.minute;
}

int GetSecond(){
	SysTime today = Clock.currTime();
	return today.second;
}