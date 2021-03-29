#include<graphics.h>
#include<stdio.h>

void line(double x1,double y1,double x2,double y2){
	double x,y,m,b;
	int cx=getmaxx()/2;
	int cy=getmaxy()/2;
	m=(y2-y1)/(x2-x1);
	b=y1-m*x1;
	if(m<=1){
		for(x=x1;x<=x2;x++){
			y=m*x+b;
			putpixel(x+cx,cy-y,10);
			}
		}
		if(m>1){
		for(y=y1;y<=y2;y++){
			x=(y-b)/m;
			putpixel(x+cx,cy-y,10);
		}
			
	}

}
int main(){
    int gd=DETECT,gm;
    initgraph(&gd,&gm,NULL);
    int xx=getmaxx()/2,yy=getmaxy()/2;
    for(int x=0;x<getmaxx();x++)
    putpixel(x,yy,10);
    for(int y=0;y<getmaxy();y++)
    putpixel(xx,y,10);
    line((getmaxx()/2)+30,(getmaxy()/2)-30,(getmaxx()/2)+300,(getmaxy()/2)-300);
    delay(5000);
    closegraph();
    return 0;
}
