#include <Keyboard.h>

/* this is the code for a keyboard - see the github file for schematics
it uses the rows as input and columns as output
as you can see, i set the schematic to do something really weird
I used Arduino bc Arduino > Micropython 
Sticky Keys are turned on by default. I'm too lazy to change that 
Inspired by Keychron q1 custom keyboard
It only works theoretically */

// set amount of rows/columns
#define ROWS 6
#define COLUMNS 15
// set column and row pins(bc they're irregular)
int row_pins[ROWS] = {10, 11, 12, 13, 14, 15};
int column_pins[COLUMNS] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 18, 19, 20, 21, 22};

// set lower alphabet(type[column][row]) - assuming that shift will automatically be called
// 0 represents a blank space
int alphabet[ROWS][COLUMNS] = {
  {177,  194,  195,  196,  197,  198,  199,  200,  201,  202,  203,  204,  205,  212,  209}, 
  {96,   1,    2,    3,    4,    5,    6,    7,    8,    9,    0,    45,   61,   178,  211},
  {179,  'q',  'w',  'e',  'r',  't',  'y',  'u',  'i',  'o',  'p',  91,   93,   92,   214},
  {193,  'a',  's',  'd',  'f',  'g',  'h',  'j',  'k',  'l',  59,   39,   '\n', 0,    210},
  {130,  'z',  'x',  'c',  'v',  'b',  'n',  'm',  44,   46,   47,   133,  218,  0,    0  },
  {128,  130,  131,  0,    0,    32,   0,    0,    135,  0,    132,  216,  217,  0,    215}
};

// set which row the output is on, whether shift and control and windows is on(0 is false)
int iteration_count = 0;
int is_shift = 0;
int is_ctrl = 0;
int is_gui = 0;

void setup(){
  // set rows as input
  for (int i = 0; i < ROWS; i++){
    pinMode(row_pins[i], INPUT);
  }

  // set columns as output
  for (int i = 0; i < 15; i++){
    pinMode(column_pins[i], OUTPUT);
  }


  // turn off all the outputs except column_0
  digitalWrite(column_pins[0], HIGH);
  for (int i = 1; i < 15; i++){
    pinMode(column_pins[i], INPUT);
  }
  Keyboard.begin();
}

void loop(){
  // very simple loop - it iterates through all row inputs to check for connected pin before moving to the next column
  for (int i = 0; i < ROWS; i++){
    if (digitalRead(row_pins[i]) == HIGH) {
      Keyboard.write(alphabet[i][iteration_count]);
      // check for shift key
      if ((i == 4 && iteration_count == 0) || (i == 4 && iteration_count == 11)) {
        is_shift = 1;

        // check for ctrl key
      } else if ((i == 5 && iteration_count == 0) || (i == 5 && iteration_count == 10)) {
        is_ctrl = 1;

        // check for windows key
      } else if ((i == 5 && iteration_count == 2) || (i == 5 && iteration_count == 8)) {
        is_gui = 1;
        
        // if something other than aforementioned buttons are pressed then release all buttons
      } else {
        Keyboard.releaseAll();
      }
    }

    // change row
    if(iteration_count < COLUMNS) {
      digitalWrite(column_pins[iteration_count], LOW);
      digitalWrite(column_pins[iteration_count + 1], HIGH);
      iteration_count++;
    } else {
      digitalWrite(column_pins[iteration_count], LOW);
      digitalWrite(column_pins[0], HIGH);
      iteration_count = 0;
    }
  }
  // standard delay for HID keyboard according to ch*tgpt
  delay(8);

  // don't touch until after tested
  delay(5000);
}