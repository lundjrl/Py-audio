#ifndef			__ZOOMJOYSTRONG__
#define			__ZOOMJOYSTRONG__

#include <SDL2/SDL.h>

//Size of the struct
#define			HEIGHT	768
#define			WIDTH	1024

//Creating a struct of colors
struct color{
	int r;
	int g;
	int b;
};
//SDL: simple directMedia layer
//A structure that contains an efficient, driver-specific representation of pixel data.
SDL_Texture* texture;
//A structure that contains a rendering state.
SDL_Renderer* renderer;
//Window for the media object
SDL_Window* window;

void setup();
void set_color( int r, int g, int b);
void point( int x, int y );
void line( int x1, int y1, int x2, int y2 );
void circle( int x, int y, int r);
void rectangle( int x, int y, int w, int h);
void finish();

#endif
