///Library Defination and Lingking Area

#include<bits/stdc++.h>
#include<graphics.h>
#include <X11/Xlib.h>
using namespace std;
//Global Defination Here


int main()
{
   int gd = DETECT, gm, midx, midy;
	XInitThreads();
   initgraph(&gd, &gm, NULL);

   setcolor(MAGENTA);
   rectangle(0,40,639,450);
   setcolor(WHITE);
   outtextxy(275,10,"Pie Chart");

   midx = getmaxx()/2;
   midy = getmaxy()/2;

   //setfillstyle(1,BLUE);
   setlinestyle(1,BLUE);
   pieslice(midx, midy, 0, 75, 100);
   outtextxy(midx+100, midy - 75, "20.83%");

   //setfillstyle(1,RED);
   setlinestyle(1,RED);
   pieslice(midx, midy, 75, 225, 100);
   outtextxy(midx-175, midy - 75, "41.67%");

   //setfillstyle(1,GREEN);
   setlinestyle(1,GREEN);
   pieslice(midx, midy, 225, 360, 100);
   outtextxy(midx+75, midy + 75, "37.50%");

   getch();
   return 0;
}
