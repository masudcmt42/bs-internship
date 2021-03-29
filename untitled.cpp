#include<graphics.h>

int main()
{
   int gd = DETECT, gm, midx, midy;

   initgraph(&gd, &gm, NULL);

   midx = getmaxx()/2;
   midy = getmaxy()/2;

   setviewport(midx - 50, midy - 50, midx + 50, midy + 50, 1);
   circle(50, 50, 55);

   getch();
   closegraph();
   return 0;
}
