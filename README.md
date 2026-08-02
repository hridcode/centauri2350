# Centauri2350

Centauri2350 is a microcontroller board based off the RP2354B chip. It has 44 usable GPIO pins, plus battery charging and an audio DAC.

This is derived from my old board named "Whistle" (which honestly was trash lmao)

## Features

- 150MHz clock speed
- 520KB RAM
- 2MB flash memory
- 48 GPIOs (4 used for onboard LED + I²S connection)
- 8 analog-capable pins
- LiPo battery charging (IP5306)
- Audio DAC (PCM5102A)
- Debug pins
- USB-C connector

## Photos

### Schematic

![PCB schematic, page 1](/photos/schematic1.png)
![PCB schematic, page 2](/photos/schematic2.png)

### PCB

![PCB layout](/photos/pcb.png)

### 3D model

![3D model of PCB](/photos/3d-render.png)

## BOM

|Part|Price|Source|
|---|---|---|
|RP2354B|1.62|[LCSC](https://www.lcsc.com/product-detail/C39843328.html)|
|PCM5102A|1.36|[LCSC](https://www.lcsc.com/product-detail/C107671.html)|
|IP5306|0.28|[LCSC](https://www.lcsc.com/product-detail/C181692.html)|
|XC6206P332MR|0.13|[LCSC](https://www.lcsc.com/product-detail/C5446.html)|
|X322512MSB4SI|0.10|[LCSC](https://www.lcsc.com/product-detail/C9002.html)|
|USB-C receptacle|0.10|[LCSC](https://www.lcsc.com/product-detail/C165948.html)|
|3.9x2.9 switch|0.15|[LCSC](https://www.lcsc.com/product-detail/C202388.html)|
|PCB|2.00|[JLCPCB](https://cart.jlcpcb.com/quote?stencilLayer=2&stencilWidth=100&stencilLength=100&stencilCounts=5&plateType=1&spm=Jlcpcb.Homepage.1010)|

## Notes

Pins marked with an asterisk (*) on the board are ADC pins.
Italicized pin names denote the debug pins.

Have fun making!