PcInt Library
=============

This is an Arduino library to administrate and handle Pin Change Interrupts as needed to allow the Mayfly to sleep and save battery power.

This is modified from the Sodaq library to work properly with SoftwareSerialMod and SDI-12Mod on the Mayfly

Examples
--------

... TODO ...
Here is a quick example to get you started

```
#include <Sodaq_PcInt.h>
void setup()
{
  pinMode(A0, INPUT_PULLUP);
  PcInt::attachInterrupt(A0, handleA0);
}

void loop()
{
  // ...
}

static uint8_t rain1ticks;
void handleA0()
{
  static bool rain1State;
  //rain counter 1
  if (digitalRead(A0) == LOW) {
    if (!rain1State) {
      rain1ticks++;
      rain1State = true;
    }
  } else {
    rain1State = false;
  }
}
```

Most important functions
------------------------
* PcInt::attachInterrupt
