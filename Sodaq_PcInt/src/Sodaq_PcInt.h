/*
 * Sodaq_PcInt.h
 *
 * This module supplies a set of helper functions to use the
 * PinChange interrupt in a convenient manner, similar to
 * the standard Arduino attachInterrupt.
 *
 * Copyright (c) 2014 Kees Bakker
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General
 * Public License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place, Suite 330,
 * Boston, MA  02111-1307  USA
 */

#ifndef SODAQ_PCINT_H_
#define SODAQ_PCINT_H_

#include <stdint.h>

class PcInt
{
public:
  static void attachInterrupt(uint8_t pin, void (*func)(void));
  static void detachInterrupt(uint8_t pin);
  static void enableInterrupt(uint8_t pin);
  static void disableInterrupt(uint8_t pin);

  // These must be public so they can be called from ISR
  static inline void handlePCINT0() __attribute__((__always_inline__));
  static inline void handlePCINT1() __attribute__((__always_inline__));
  static inline void handlePCINT2() __attribute__((__always_inline__));
  static inline void handlePCINT3() __attribute__((__always_inline__));

  // For diagnostic purposes
  static void (*getFunc(uint8_t group, uint8_t nr))(void);
private:
  static void   (*_funcs0[8])(void);
#if defined(PCINT1_vect)
  static void   (*_funcs1[8])(void);
#endif
#if defined(PCINT2_vect)
  static void   (*_funcs2[8])(void);
#endif
#if defined(PCINT3_vect)
  static void   (*_funcs3[8])(void);
#endif
};

#endif /* SODAQ_PCINT_H_ */
