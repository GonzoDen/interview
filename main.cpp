#include <ncurses.h>

bool isExit(int ch) 
{
	return ch == 'q';
}

int main()
{
	//setting up the terminal window
	initscr();
	keypad(stdscr, TRUE);
	cbreak();
	noecho();
	curs_set();

	int y, x;
	x = COLS / 2;
	y = LINES / 2;
	refresh();

	WINDOW* winwin = nullptr;

	int sobaka = '@';
	int ch;
	

	while(!isExit (ch = getch()))
	{
		if (winwin != nullptr)
			delwin(winwin);
		switch(ch)
		{
			case UP:
				if (y == 0) {
					y = y
				}
				else 
				{
					y = y-1
				}
			case DOWN:
				if (y == LINES-1) {
					y = y
				}
				else 
				{
					y = y+1
				}
			case KEY_RIGHT:
			if (x == 0) {
					x = x
				}
				else 
				{
					x = x-1
				}
			case KEY_LEFT:
				if (x == COLS-1) {
					x = x
				}
				else 
				{
					x = x-1
				}
		}

		WINDOW* winwin = newwin(1, 2, y, x);
		waddch(winwin, sobaka);
		wrefresh(winwin);
	}

	endwin();
	return 0;
}